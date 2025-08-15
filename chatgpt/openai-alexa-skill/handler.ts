import {
  ErrorHandler,
  HandlerInput,
  RequestHandler,
  SkillBuilders,
} from 'ask-sdk-core';
import {
  Response,
} from 'ask-sdk-model';
import 'source-map-support/register';
import chatgpt from './chatgpt.ts';

const ErrorHandler : ErrorHandler = {
  canHandle(handlerInput : HandlerInput, error : Error ) : boolean {
    return true;
  },
  handle(handlerInput : HandlerInput, error : Error) : Response {
    console.error('error!!!');
    console.error(error);

    return handlerInput.responseBuilder
      .speak('すみません。コマンドを理解できませんでした。もう一度言ってください。')
      .reprompt('すみません。コマンドを理解できませんでした。もう一度言ってください。')
      .getResponse();
  }
};

const LaunchRequestHandler : RequestHandler = {
  canHandle(handlerInput : HandlerInput) : boolean {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'LaunchRequest';        
  },
  handle(handlerInput : HandlerInput) : Response {
    const speechText = '会話ボットを起動しました。質問してください。';

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(speechText)
      .withSimpleCard(speechText, speechText)
      .getResponse();
  },
};

const PromptIntentHandler : RequestHandler = {
  canHandle(handlerInput : HandlerInput) : boolean {
    const request = handlerInput.requestEnvelope.request;  
    return request.type === 'IntentRequest'
      && request.intent.name === 'PromptIntent';
  },
  async handle(handlerInput : HandlerInput) : Promise<Response> {
    const request = handlerInput.requestEnvelope.request;  
    if (request.type !== 'IntentRequest') return;

    try {
      let sessionAttributes = handlerInput.attributesManager.getSessionAttributes();
      if (!('messages' in sessionAttributes)) {
        sessionAttributes.messages = [
          {"role": "system", "content": "あなたはスマートスピーカーです。150文字以内で回答してください。"},
        ];
      }
      const question = request.intent.slots.Content.value;
      sessionAttributes.messages.push(
        {"role": "user", "content": question},
      );      
      const resonseContent = await chatgpt.createChat(sessionAttributes.messages);
      sessionAttributes.messages.push(
        {"role": "assistant", "content": resonseContent}
      );
      handlerInput.attributesManager.setSessionAttributes(sessionAttributes);        
      return handlerInput.responseBuilder
      .speak(resonseContent)
      .reprompt('何か問いかけてみてください')
      .withSimpleCard('回答', resonseContent)
      .getResponse();   
    } catch (e) {
      console.error(e)
    }           
  },
};

const CancelAndStopIntentHandler : RequestHandler = {
  canHandle(handlerInput : HandlerInput) : boolean {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && (request.intent.name === 'AMAZON.CancelIntent'
          || request.intent.name === 'AMAZON.StopIntent');
  },
  handle(handlerInput : HandlerInput) : Response {
    const speechText = 'これで会話ボットを終了します';
    console.log('bye!!')
    return handlerInput.responseBuilder
      .speak(speechText)
      .withSimpleCard(speechText, speechText)
      .withShouldEndSession(true)      
      .getResponse();
  },
};

export const alexa = SkillBuilders.custom()
  .addRequestHandlers(
    LaunchRequestHandler,
    PromptIntentHandler,
    CancelAndStopIntentHandler,
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();