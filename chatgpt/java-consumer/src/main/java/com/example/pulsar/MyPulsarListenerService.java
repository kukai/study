package com.example.pulsar;

import org.apache.pulsar.client.api.Consumer;
import org.apache.pulsar.client.api.Message;
import org.apache.pulsar.client.api.PulsarClient;
import org.apache.pulsar.client.api.SubscriptionType;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;

@Service
public class MyPulsarListenerService {

    private PulsarClient client;
    private Consumer<byte[]> consumer;

    @PostConstruct
    public void init() throws Exception {
        client = PulsarClient.builder()
                .serviceUrl("pulsar://localhost:6650")
                .build();

        consumer = client.newConsumer()
                .topic("my-topic")
                .subscriptionName("my-subscription")
                .subscriptionType(SubscriptionType.Shared)
                .subscribe();

        startListening();
    }

    public void startListening() {
        Thread listenerThread = new Thread(() -> {
            while (true) {
                try {
                    Message<byte[]> msg = consumer.receive();
                    String content = new String(msg.getData());
                    System.out.println("Received message: " + content);
                    consumer.acknowledge(msg);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        listenerThread.start();
    }
}
