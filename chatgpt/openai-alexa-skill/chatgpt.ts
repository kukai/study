const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);


const createChat = async (messages: any): Promise<string> => {
    console.log('messages', messages);
    const res = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages,
    });
    const responseContent = res.data.choices[0].message.content;
    console.log('"' + responseContent + '"');
    return responseContent;
}

export default {
    createChat
}