from src.chatbot import chat_with_rag

def test_chatbot():
    response = chat_with_rag("What is Tesla known for?")
    assert isinstance(response, str)
    assert len(response) > 0

test_chatbot()