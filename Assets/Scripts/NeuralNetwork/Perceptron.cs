using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Perceptron
{
    private int numberOfWeights;
    private float[] weights;
    public Perceptron(int numberOfWeights){
        this.numberOfWeights = numberOfWeights;
        this.weights = createWeights();
    }
    public Perceptron(int numberOfWeights, float[] weights){
        this.numberOfWeights = numberOfWeights;
        this.weights = weights;
    }
    public float[] createWeights(){
        float[] weights = new float[numberOfWeights];
        for(int i=0; i<numberOfWeights; i++){
            weights[i] = Random.Range(-1f,1.1f);
        }
        return weights;
    }
    public float createSum(float[] inputs){
        float sum = 0;
        for(int i=0; i<numberOfWeights; i++){
            sum += (inputs[i] * weights[i]);
        }
        return sum;
    }
    public float[] getWeights(){
        return weights;
    }
}
