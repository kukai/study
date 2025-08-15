let audioContext = new (window.AudioContext || window.webkitAudioContext)();
let noiseSource = null;
let b0, b1, b2, b3, b4, b5, b6;

function resetPinkNoiseVariables() {
  b0 = b1 = b2 = b3 = b4 = b5 = b6 = 0.0;
}

function generatePinkNoise(output) {
  for (let i = 0; i < output.length; i++) {
    let white = Math.random() * 2 - 1;

    b0 = 0.99886 * b0 + white * 0.0555179;
    b1 = 0.99332 * b1 + white * 0.0750759;
    b2 = 0.96900 * b2 + white * 0.1538520;
    b3 = 0.86650 * b3 + white * 0.3104856;
    b4 = 0.55000 * b4 + white * 0.5329522;
    b5 = -0.7616 * b5 - white * 0.0168980;
    output[i] = b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362;
    output[i] *= 0.11; // (roughly) compensate for gain
    b6 = white * 0.115926;
  }
}

let gainNode = audioContext.createGain();  // Create a GainNode
gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);  // Set the default volume to 20%

function playNoise(type) {
  stopNoise(); // Stop any ongoing noise
  
  noiseSource = audioContext.createBufferSource();
  const bufferSize = audioContext.sampleRate,  // Reduced buffer size
        noiseBuffer = audioContext.createBuffer(1, bufferSize, audioContext.sampleRate),
        output = noiseBuffer.getChannelData(0);
  
  if (type === 'white') {
    for (let i = 0; i < bufferSize; i++) {
      output[i] = Math.random() * 2 - 1;
    }
  } else if (type === 'pink') {
    resetPinkNoiseVariables();
    generatePinkNoise(output);
  } else if (type === 'brown') {
    // Implement brown noise algorithm here
  }
  
  noiseSource.buffer = noiseBuffer;
  noiseSource.loop = true;
  noiseSource.connect(gainNode);  // Connect the noise source to the gain node
  gainNode.connect(audioContext.destination);  // Connect the gain node to the destination
  
  noiseSource.start();
}

function stopNoise() {
  if (noiseSource) {
    noiseSource.stop();
    noiseSource.disconnect();
  }
}

// Function to set the volume
function setVolume(volume) {
  gainNode.gain.setValueAtTime(volume, audioContext.currentTime);
}
