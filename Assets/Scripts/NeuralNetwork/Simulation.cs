using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Simulation
{
    private Brain brain;
    private int carsNorth;
    private int carsEast;
    private int carsSouth;
    private int carsWest;
    private int points;
    private int currentState;
    public Simulation(){
        brain = new Brain();
        points = 0;
    }
    public Simulation(float[][] weights){
        brain = new Brain(weights);
        points = 0;
    }
    public void addCars(){
        int randomChoice = (int)(Random.Range(0,4));
        int randomCars = (int)(Random.Range(1,5));
        switch(randomChoice){
            case 0:
                carsNorth += randomCars;
            break;
            case 1:
                carsEast += randomCars;
            break;
            case 2:
                carsSouth += randomCars;
            break;
            case 3:
                carsWest += randomCars;
            break;
        }
    }
    public void carControl(){
        currentState = getLightState(new float[]{carsNorth,carsEast,carsSouth,carsWest});
        if(currentState == 1){
            for(int i=0; i<2; i++){
                if(carsNorth > 0){carsNorth--;}
                if(carsSouth > 0){carsSouth--;}
            }
        }
        else{
            for(int i=0; i<2; i++){
                if(carsEast > 0){carsEast--;}
                if(carsWest > 0){carsWest--;}
            }
        }
        this.points += carsNorth + carsEast + carsSouth + carsWest;
    }
    public int[] getCars(){
        return new int[]{carsNorth,carsEast,carsSouth,carsWest};
    }
    public int getCurrentState(){
        return currentState;
    }
    public int getLightState(float[] inputs){
        return this.brain.chooseState(inputs);
    }
    public int getScore(){
        return points;
    }
    public float[][] getWeights(){
        return brain.getWeights();
    }
}
