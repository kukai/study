import React, { useEffect, useState } from "react";
import axios from "axios";

interface Message {
    role: string;
    content: string;
}

const App: React.FC = () => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [newMessage, setNewMessage] = useState("");

    const sendMessage = async () => {
        const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:3001/chat";
        const { data } = await axios.post(apiUrl, {
            role: "user",
            content: newMessage,
        });
        setMessages(data.messages);
        setNewMessage("");
    };

    return (
        <div>
            <div>
                {messages.map((message, index) => (
                    <div key={index}>
                        <b>{message.role}:</b> {message.content}
                    </div>
                ))}
            </div>
            <div>
                <input
                    type="text"
                    value={newMessage}
                    onChange={(e) => setNewMessage(e.target.value)}
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default App;
