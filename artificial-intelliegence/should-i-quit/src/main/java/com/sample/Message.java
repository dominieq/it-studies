package com.sample;

public class Message {

    private String question;
    private String answer;

    public Message() {
    }

    public Message(String question, String answer) {
        this.question = question;
        this.answer = answer;
    }

    public String getQuestion() {
        return question;
    }

    public void setQuestion(String printMessage) {
        this.question = printMessage;
    }

    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
}