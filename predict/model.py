def predict(input):
    # from google.colab import drive
    # drive.mount('/content/drive')
    
    import tensorflow as tf
    from tensorflow import keras
    from keras.models import load_model
    from keras.preprocessing import sequence
    # from tensorflow.keras.preprocessing.text import Tokenizer
    # from tensorflow.keras.preprocessing.sequence import pad_sequences
    # from tensorflow.keras.preprocessing.sequence import pad_sequences
    from keras_preprocessing.sequence import pad_sequences

    model = tf.keras.models.load_model('model.h5')

    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    input
    import pickle

    # loading
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    input = tokenizer.texts_to_sequences(input)
    input = pad_sequences(input, maxlen=120)

    output = (model.predict(input) >=0.5).astype(int)

    print(output)

    from json import JSONEncoder
    import numpy

    class NumpyArrayEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)

    import json

    last = json.dumps(output, cls=NumpyArrayEncoder)
    if last == "[[1]]":
        last = "Included"
    elif last == "[[0]]": 
        last = "Excluded"

    jsonoutput = {
        "Prediction" : last
    }

    dump = json.dumps(jsonoutput)

    return dump