def GenerateData(k,l, number):
    import tensorflow as tf
    import itertools
    mnist = tf.keras.datasets.mnist  # 28x28 images of handwritten digits 0-9
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    Input_Data = []
    Output_Data =[]
    Data=[]
    i = 0
    j = 0
    while i < number:
        if (y_train[j] == k or y_train[j]==l) :
            local=list(itertools.chain(*x_train[j]))
            Input_Data.append(local)
            Output_Data.append(y_train[j])
            i=i+1
        j=j+1
    Data=[Input_Data, Output_Data]
    return Data


ok=GenerateData(1,2,100)
print(ok[0])
print(ok[1])
print(len(ok[0]))
print(len(ok[1]))