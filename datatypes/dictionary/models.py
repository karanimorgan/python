ai_models = {
    "gpt-3.5-turbo":{
        "Max_tokens":4096,
    "cost_per_1k_tokens": 0.002,
    "training_words": ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice"]
    },
"gpt-4": {
    "max_tokens": 8192,
    "cost_per_1k_tokens": 0.03,
    "training_words":["Monday", "Tuesday", "wednesday", "Thursday", "Friday", "saturday", "sunday"]
}}

print(ai_models["gpt-3.5-turbo"]["training_words"][1])
# print(ai_models)
# print(ai_models)
