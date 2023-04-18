using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Intersection : MonoBehaviour
{
    List<int> neighbors = new List<int>();
    public void addNeighbor(int newIntersection){
        neighbors.Add(newIntersection);
    }
    public string neighborsToString(){
        string neighborString = "";
        for(int i=0; i<neighbors.Count; i++){
            if(i!= 0){
                neighborString += ",";
            }
            neighborString += neighbors[i];
        }
        return neighborString;
    }
}
