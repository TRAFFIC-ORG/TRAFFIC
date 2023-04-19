using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PregenControll : MonoBehaviour
{
    [SerializeField] private GameObject roadPrefab, nodesPrefab, nodeHolder, simControll;
    List<GameObject> nodes; 
    // Start is called before the first frame update
    void Start()
    {
        nodes = new List<GameObject>();
        int horizontalRoad = 5;
        int verticalRoad = 7;
        //HorizontalRoads
        float currentY = 3.5f;
        for(int i = 0; i<horizontalRoad; i++){
            GameObject newRoad = Instantiate(roadPrefab, new Vector3(0,0,0),Quaternion.identity, this.transform);
            LineRenderer newLine = newRoad.GetComponent<LineRenderer>();
            newLine.SetPosition(0, new Vector3(-12,currentY,0));
            newLine.SetPosition(1, new Vector3(12,currentY,0));
            currentY -= 2;
        }
        float currentX = -6.5f;
        for(int i = 0; i<verticalRoad; i++){
            GameObject newRoad = Instantiate(roadPrefab, new Vector3(0,0,0),Quaternion.identity,this.transform);
            LineRenderer newLine = newRoad.GetComponent<LineRenderer>();
            newLine.SetPosition(0, new Vector3(currentX,-5,0));
            newLine.SetPosition(1, new Vector3(currentX,5,0));
            currentX +=2;
        }
        float nodeY = 3.5f;
        float nodeX = -6.5f;
        int currentNode = 0;
        for(int i=0; i<horizontalRoad; i++){
            for(int j=0; j<verticalRoad; j++){
                GameObject newNode = Instantiate(nodesPrefab, new Vector3(nodeX,nodeY,0), Quaternion.identity, nodeHolder.transform);
                newNode.name = currentNode+"";
                nodes.Add(newNode);
                nodeX +=2;
                currentNode++;
            }
            nodeX = -6.5f;
            nodeY -= 2;
        }
        for(int i=0; i<nodes.Count; i++){
            List<Node> neighbors = new List<Node>();
            //If i is not in the first row
            if(i > 6){
                //They will have a northern neighbor
                neighbors.Add(nodes[i-7].GetComponent<Node>());
            }
            //If i is not in the last row
            if(i < 28){
                //They will have a southern neighbor
                neighbors.Add(nodes[i+7].GetComponent<Node>());
            }
            //if(i%)
            if(i%7 != 0){
                //They will have a western neighbor
                neighbors.Add(nodes[i-1].GetComponent<Node>());
            }
            if(i%7 != 6){
                //They will have a eastern neighbor
                neighbors.Add(nodes[i+1].GetComponent<Node>());
            }
            nodes[i].GetComponent<Node>().setNeighbors(neighbors);
        }
        simControll.GetComponent<SimControl>().setNodes(nodes);
    }
}
