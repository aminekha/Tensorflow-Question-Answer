import os
import tensorflow as tf
import tensorflow_text  # Required to run exported model.

class QuestionAnswer:
    def __init__(self):
        pass
    MODEL = "t5.1.1.small_ssm_nq" #@param["t5.1.1.small_ssm_nq", "t5.1.1.xl_ssm_nq", "t5.1.1.xxl_ssm_nq"]
    saved_model_dir = f"qa_app/core/weights/{MODEL}"
    saved_model_path = os.path.join(saved_model_dir, max(os.listdir(saved_model_dir)))

    model = tf.saved_model.load(saved_model_path, ["serve"])

    def predict_fn(x):
        return QuestionAnswer.model.signatures['serving_default'](tf.constant(x))['outputs'].numpy()

    def answer(question):
        return QuestionAnswer.predict_fn([question])[0].decode('utf-8')


# user_question = input("Question: ")
# print("The answer is:", answer(user_question))