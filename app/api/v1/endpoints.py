from flask import Blueprint, render_template, request, Response
from app.services.question_answering import get_rag_chain


rag_chain = get_rag_chain()

api_v1 = Blueprint("api_v1", __name__)

@api_v1.route("/")
def index():
    return render_template("index.html")

@api_v1.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    
    def generate():
        # Stream the response chunk by chunk
        for chunk in rag_chain.stream(msg):
            yield chunk

    # Return a streaming response
    return Response(generate(), content_type="text/plain")