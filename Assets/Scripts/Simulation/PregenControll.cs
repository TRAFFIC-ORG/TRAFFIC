using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PregenControll : MonoBehaviour
{
    [SerializeField] private GameObject roadPrefab, nodesPrefab, nodeHolder;
    List<GameObject> nodes; 
    // Start is called before the first frame update
    void Start()
    {
        nodes = new List<GameObject>();
        int horizontalRoad = 10;
        int verticalRoad = 15;
        //HorizontalRoads
        float currentY = 3.5f;
        for(int i = 0; i<horizontalRoad; i++){
            GameObject newRoad = Instantiate(roadPrefab, new Vector3(0,0,0),Quaternion.identity, this.transform);
            LineRenderer newLine = newRoad.GetComponent<LineRenderer>();
            newLine.SetPosition(0, new Vector3(-12,currentY,0));
            newLine.SetPosition(1, new Vector3(12,currentY,0));
            currentY --;
        }
        float currentX = -6.5f;
        for(int i = 0; i<verticalRoad; i++){
            GameObject newRoad = Instantiate(roadPrefab, new Vector3(0,0,0),Quaternion.identity,this.transform);
            LineRenderer newLine = newRoad.GetComponent<LineRenderer>();
            newLine.SetPosition(0, new Vector3(currentX,-5,0));
            newLine.SetPosition(1, new Vector3(currentX,5,0));
            currentX ++;
        }
        float nodeY = 3.5f;
        float nodeX = -6.5f;
        for(int i=0; i<horizontalRoad; i++){
            for(int j=0; j<verticalRoad; j++){
                GameObject newNode = Instantiate(nodesPrefab, new Vector3(nodeX,nodeY,0), Quaternion.identity, nodeHolder.transform);
                nodes.Add(newNode);
                nodeX ++;
            }
            nodeX = -6.5f;
            nodeY --;
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
