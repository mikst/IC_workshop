import numpy
import pyttsx3

data=[
[ 488 , 478 , 424 , 367 , 0 ],
[ 488 , 480 , 424 , 388 , 0 ],
[ 465 , 467 , 426 , 383 , 0 ],
[ 476 , 481 , 423 , 360 , 0 ],
[ 475 , 475 , 435 , 369 , 0 ],
[ 478 , 476 , 409 , 374 , 0 ],
[ 621 , 477 , 417 , 572 , 1 ],
[ 650 , 485 , 410 , 586 , 1 ],
[ 662 , 481 , 406 , 597 , 1 ],
[ 651 , 474 , 421 , 599 , 1 ],
[ 668 , 495 , 408 , 592 , 1 ],
[ 667 , 471 , 421 , 606 , 1 ],
[ 660 , 474 , 425 , 604 , 1 ],
[ 650 , 479 , 410 , 609 , 1 ],
[ 655 , 472 , 398 , 607 , 1 ],
[ 656 , 481 , 425 , 610 , 1 ],
[ 640 , 493 , 430 , 618 , 1 ],
[ 654 , 496 , 429 , 621 , 1 ],
[ 650 , 502 , 427 , 609 , 1 ],
[ 650 , 484 , 430 , 604 , 1 ],
[ 653 , 499 , 418 , 597 , 1 ],
[ 453 , 474 , 419 , 354 , 0 ],
[ 445 , 449 , 406 , 358 , 0 ],
[ 432 , 481 , 419 , 342 , 0 ],
[ 454 , 462 , 406 , 359 , 0 ],
[ 470 , 467 , 426 , 366 , 0 ],
[ 477 , 473 , 406 , 366 , 0 ],
[ 476 , 472 , 421 , 369 , 0 ],
[ 473 , 477 , 416 , 357 , 0 ],
[ 465 , 478 , 438 , 373 , 0 ],
[ 473 , 478 , 431 , 391 , 0 ],
[ 472 , 474 , 410 , 351 , 0 ],
[ 458 , 465 , 406 , 372 , 0 ],
[ 625 , 473 , 414 , 537 , 1 ],
[ 625 , 460 , 416 , 573 , 1 ],
[ 628 , 462 , 422 , 569 , 1 ],
[ 655 , 471 , 414 , 582 , 1 ],
[ 621 , 477 , 400 , 575 , 1 ],
[ 617 , 480 , 417 , 581 , 1 ],
[ 617 , 468 , 420 , 583 , 1 ],
[ 626 , 488 , 428 , 591 , 1 ],
[ 617 , 476 , 430 , 593 , 1 ],
[ 621 , 479 , 418 , 585 , 1 ],
[ 619 , 475 , 425 , 588 , 1 ]
]



class Neuron:

    def __init__(self, id):
        self.weights = []
        self.bias = numpy.random.randn()
        self.output_value=0
        self.temp_value=0
        self.inputNeurons= []
        self.outputNeurons= []
        self.id = id
        self.learningRate=0.2

    def setInput(self, inputNeuron):
        self.inputNeurons.append(inputNeuron)
        self.weights.append(numpy.random.randn())

    def forwardUpdate(self):
        out=0
        for n in range(len(self.inputNeurons)):
            out += self.inputNeurons[n].getValue() * self.weights[n]
        self.temp_value = out + self.bias
        self.output_value = self.sigmoid(self.temp_value)

    def sigmoid(self, x):
        return 1/(1+numpy.exp(-x))

    def getValue(self):
        return self.output_value

    def setValue(self, input=0):
        self.output_value = input

    def dump(self):
        print("id: ", self.id + 1)
        #print("output: ", self.output_value)
        #print("value: ", self.temp_value)
        print("weights: ", self.weights)
        print("bias: ", self.bias)
        #print("number of inputs: ", len(self.inputNeurons))


    def backPropagation(self, target, output):
        if output == 1:
            #bring derivative through square function
            dcost_dpred = 2* (self.output_value - target)
        else:
            dcost_dpred = target

        #bring derivative through sigmoid (prediction is sigmoid)
        #dpred_dz = sigmoid(z) * (1-sigmoid(z))
        dpred_dz = self.output_value * (1-self.output_value)
        # adjust the bias
        self.bias-=self.learningRate*dcost_dpred*dpred_dz


        for i in range(len(self.weights)):
            self.inputNeurons[i].backPropagation( dcost_dpred*dpred_dz * self.weights[i],0)
            #adjust the weights
            self.weights[i]-=self.learningRate * dcost_dpred*dpred_dz * self.inputNeurons[i].output_value






input_neurons = []
hidden1_neurons = []
hidden2_neurons = []
hidden3_neurons = []
output_neurons = []

def connectNetwork():
    for i in range (4):
        input_neurons.append(Neuron(i))
    for i in range (4):
        hidden1_neurons.append(Neuron(i))
    for i in range (4):
        hidden2_neurons.append(Neuron(i))
    for i in range (4):
        hidden3_neurons.append(Neuron(i))
    for i in range (1):
        output_neurons.append(Neuron(i))

    hidden1_neurons[0].setInput(input_neurons[0])
    hidden1_neurons[0].setInput(input_neurons[1])
    hidden1_neurons[0].setInput(input_neurons[2])
    hidden1_neurons[0].setInput(input_neurons[3])

    hidden1_neurons[1].setInput(input_neurons[0])
    hidden1_neurons[1].setInput(input_neurons[2])
    hidden1_neurons[1].setInput(input_neurons[1])
    hidden1_neurons[1].setInput(input_neurons[3])

    hidden1_neurons[2].setInput(input_neurons[0])
    hidden1_neurons[2].setInput(input_neurons[1])
    hidden1_neurons[2].setInput(input_neurons[2])
    hidden1_neurons[2].setInput(input_neurons[3])

    hidden1_neurons[3].setInput(input_neurons[0])
    hidden1_neurons[3].setInput(input_neurons[2])
    hidden1_neurons[3].setInput(input_neurons[1])
    hidden1_neurons[3].setInput(input_neurons[3])


    hidden2_neurons[0].setInput(hidden1_neurons[0])
    hidden2_neurons[0].setInput(hidden1_neurons[1])
    hidden2_neurons[0].setInput(hidden1_neurons[2])
    hidden2_neurons[0].setInput(hidden1_neurons[3])

    hidden2_neurons[1].setInput(hidden1_neurons[0])
    hidden2_neurons[1].setInput(hidden1_neurons[1])
    hidden2_neurons[1].setInput(hidden1_neurons[2])
    hidden2_neurons[1].setInput(hidden1_neurons[3])

    hidden2_neurons[2].setInput(hidden1_neurons[0])
    hidden2_neurons[2].setInput(hidden1_neurons[1])
    hidden2_neurons[2].setInput(hidden1_neurons[2])
    hidden2_neurons[2].setInput(hidden1_neurons[3])

    hidden2_neurons[3].setInput(hidden1_neurons[0])
    hidden2_neurons[3].setInput(hidden1_neurons[1])
    hidden2_neurons[3].setInput(hidden1_neurons[2])
    hidden2_neurons[3].setInput(hidden1_neurons[3])

    hidden3_neurons[0].setInput(hidden2_neurons[0])
    hidden3_neurons[0].setInput(hidden2_neurons[1])
    hidden3_neurons[0].setInput(hidden2_neurons[2])
    hidden3_neurons[0].setInput(hidden2_neurons[3])

    hidden3_neurons[1].setInput(hidden2_neurons[0])
    hidden3_neurons[1].setInput(hidden2_neurons[1])
    hidden3_neurons[1].setInput(hidden2_neurons[2])
    hidden3_neurons[1].setInput(hidden2_neurons[3])

    hidden3_neurons[2].setInput(hidden2_neurons[0])
    hidden3_neurons[2].setInput(hidden2_neurons[1])
    hidden3_neurons[2].setInput(hidden2_neurons[2])
    hidden3_neurons[2].setInput(hidden2_neurons[3])

    hidden3_neurons[3].setInput(hidden2_neurons[0])
    hidden3_neurons[3].setInput(hidden2_neurons[1])
    hidden3_neurons[3].setInput(hidden2_neurons[2])
    hidden3_neurons[3].setInput(hidden2_neurons[3])


    output_neurons[0].setInput(hidden3_neurons[0])
    output_neurons[0].setInput(hidden3_neurons[1])
    output_neurons[0].setInput(hidden3_neurons[2])
    output_neurons[0].setInput(hidden3_neurons[3])

connectNetwork()

def training(cycle):
    for i in range (cycle):
        # pick random data point
        num=numpy.random.randint(low=0,high=42)
        for t in range (len(input_neurons)):
            input_neurons[t].setValue(data[num][t]/1023)

        for neuron in hidden1_neurons:
            neuron.forwardUpdate()

        for neuron in hidden2_neurons:
            neuron.forwardUpdate()

        for neuron in hidden3_neurons:
            neuron.forwardUpdate()

        for neuron in output_neurons:
            neuron.forwardUpdate()

        for t in range(1):
            if data[num][4] == 1:
                output_neurons[t].backPropagation(1,1)
            else:
                output_neurons[t].backPropagation(0,1)



training(8000)
print("----layer 1-------")
for neuron in hidden1_neurons:
    neuron.dump()
print("----layer 2-------")
for neuron in hidden2_neurons:
    neuron.dump()
print("----layer 3-------")
for neuron in hidden3_neurons:
    neuron.dump()
print("----output-------")
for neuron in output_neurons:
   neuron.dump()

sensor=[0,0,0,0]

while True:

    si = input("sensor inputs?\n")
    sensor = [float(numeric_string) for numeric_string in si.split(",")]
    #print(sensor)

    if len(sensor) != len(input_neurons):
        print("please provide inputs: ", len(input_neurons))
        continue

    for t in range(len(input_neurons)):
        input_neurons[t].setValue(sensor[t])


    for t in range (4):
        input_neurons[t].setValue(sensor[t]/1023)

    for neuron in hidden1_neurons:
        neuron.forwardUpdate()

    for neuron in hidden2_neurons:
        neuron.forwardUpdate()

    for neuron in hidden3_neurons:
        neuron.forwardUpdate()

    for neuron in output_neurons:
        neuron.forwardUpdate()

    print("out1: ", output_neurons[0].output_value)
