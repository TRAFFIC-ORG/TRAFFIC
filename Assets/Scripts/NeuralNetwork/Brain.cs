using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Brain
{
    private ArrayList perceptrons;
    private float[][] weights;
    public Brain(){
        perceptrons = new ArrayList();
        perceptrons.Add(new Perceptron(4));
        perceptrons.Add(new Perceptron(4));
        perceptrons.Add(new Perceptron(2));
    }
    public Brain(float[][] weights){
        this.weights = weights;
        perceptrons = new ArrayList();
        perceptrons.Add(new Perceptron(4, weights[0]));
        perceptrons.Add(new Perceptron(4, weights[1]));
        perceptrons.Add(new Perceptron(2, weights[2]));
    }
    public int chooseState(float[] inputs){
        Perceptron per1 = (Perceptron)perceptrons[0];
        Perceptron per2 = (Perceptron)perceptrons[1];
        Perceptron per3 = (Perceptron)perceptrons[2];

        float perSum1 = per1.createSum(inputs);
        float perSum2 = per2.createSum(inputs);
        float finalSum = per3.createSum(new float[]{perSum1,perSum2});

        int output = 0;
        if(finalSum >= 0){
            output = 1;
        }
        else{
            output = -1;
        }

        return output;
    }
    public float[][] getWeights(){
        float[][] allWeights = new float[perceptrons.Count][];
        for(int i=0; i<perceptrons.Count; i++){
            Perceptron currentPer = (Perceptron)perceptrons[i];
            allWeights[i] = currentPer.getWeights();
        }
        return allWeights;
    }
}
