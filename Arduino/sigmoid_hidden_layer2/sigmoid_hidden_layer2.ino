float my_weight1; 
float my_weight2;
float my_bias;

float input1;
float input2;

float output;

float error_from_layer2;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
delay(1000);

forwardProp();
//backProp();

}

void loop() {
  // put your main code here, to run repeatedly:

}

void forwardProp(){
float temp = my_weight1 * input1 + my_weight2 * input2  + my_bias ;
float sigmoid = 1.0 / (1.0 + exp(-1.0 * temp));
Serial.print("temp = ");
Serial.print(temp);
Serial.print(" : output = ");
Serial.println(sigmoid,4);
}

void backProp(){
  //back propagation for hidden layer1
//here is the difference for hidde layer
//the derivative of cost is calculated from previous layer
float dcost_dpred = error_from_layer2;
float dpred_dz = output * (1-output);
Serial.print("dpred_dz = ");
Serial.println(dpred_dz);

// derivative of cost of connected layer, calculate it to pass on
float dcost_input1 = dcost_dpred * dpred_dz* my_weight1;
float dcost_input2 = dcost_dpred * dpred_dz* my_weight2;


Serial.print("pass this error amout to hidden1 neuron0: ");
Serial.println(dcost_input1,4);
Serial.print("pass this error amout to hidden1 neuron1: ");
Serial.println(dcost_input2,4);


// cost of each input*weight
float dcost_dw_1=dcost_dpred*dpred_dz*input1;
float dcost_dw_2=dcost_dpred*dpred_dz*input2;
float dcost_db  =dcost_dpred*dpred_dz;

// adjust the weight and bias, calculate how much it needs to adjust
my_weight1 = my_weight1 - dcost_dw_1 * 0.2;
my_weight2 = my_weight2 - dcost_dw_2 * 0.2;
my_bias    = my_bias - dcost_db * 0.2;

Serial.print("float my_weight1 = ");
Serial.println(my_weight1,4); 
Serial.print("float my_weight2 = ");
Serial.println(my_weight2,4); 
Serial.print("float my_bias = ");
Serial.println(my_bias,4); 
}
