using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System.IO;
public class CustomControl : MonoBehaviour
{
    [SerializeField] private GameObject intersectionPrefab, roadPrefab, simControl, nodePrefab, nodeHolder;
    private List<GameObject> intersections;
    private List<GameObject> roads;
    List<GameObject> nodes; 
    private SimControl controller;
    // Start is called before the first frame update
    void Start()
    {
        intersections = new List<GameObject>();
        nodes = new List<GameObject>();
        roads = new List<GameObject>();
        controller = simControl.GetComponent<SimControl>();
        loadMap();
        for(int i = 0; i<intersections.Count; i++){
            nodes.Add(Instantiate(nodePrefab,intersections[i].transform.position,Quaternion.identity,nodeHolder.transform));
        }
    }
    public void loadMap(){
        string currentMap = controller.getMapName();
        if(currentMap != ""){
            List<string> mapStrings = ReadFile(currentMap);
            if(mapStrings != null){
                for(int i = 0; i<mapStrings.Count; i++){
                    string[] line = mapStrings[i].Split(":");
                    if(line[0] == "I"){
                        string[] pos = line[1].Split(",");
                        intersections.Add(Instantiate(intersectionPrefab,new Vector3(float.Parse(pos[0]),float.Parse(pos[1]),0),Quaternion.identity));
                        intersections[intersections.Count-1].name = intersections.Count+"";
                    }
                    else if(line[0] == "R"){
                        string[] pos1 = line[1].Split(",");
                        string[] pos2 = line[2].Split(",");
                        roads.Add(Instantiate(roadPrefab, Vector3.zero, Quaternion.identity));
                        LineRenderer currentLine = roads[roads.Count - 1].GetComponent<LineRenderer>();

                        Vector3 point1 = new Vector3(float.Parse(pos1[0]), float.Parse(pos1[1]), 0);
                        Vector3 point2 = new Vector3(float.Parse(pos2[0]), float.Parse(pos2[1]), 0);

                        Vector3 lineDirection = point2 - point1;
                        float segment1Length = lineDirection.magnitude * 0.05f;
                        float segment2Length = lineDirection.magnitude * 0.9f;

                        Vector3 segment1End = point1 + lineDirection.normalized * segment1Length;
                        Vector3 segment2Start = segment1End + lineDirection.normalized * (lineDirection.magnitude * 0.05f);
                        Vector3 segment2End = point2 - lineDirection.normalized * segment1Length;

                        currentLine.positionCount = 4;
                        currentLine.SetPosition(0, point1);
                        currentLine.SetPosition(1, segment1End);
                        currentLine.SetPosition(2, segment2End);
                        currentLine.SetPosition(3, point2);
                    }
                }
            }
            else{
                Debug.Log("Please input a valid map name");
            }
        }
        else{
            Debug.Log("Please input a map name");
        }
    }
    public static List<string> ReadFile(string selectedMap)
    {
        List<string> mapStrings = new List<string>();
        string folderPath = Application.persistentDataPath + "/Maps/";
        if (!Directory.Exists(folderPath)) {
            Directory.CreateDirectory(folderPath);
        }
        string path = folderPath + selectedMap + ".txt";
        if(File.Exists(path)){
            StreamReader reader = new StreamReader(path);
            while(!reader.EndOfStream){
                string currentLine = reader.ReadLine();
                mapStrings.Add(currentLine);
            }
            reader.Close();
            return mapStrings;
        }
        return null;
    }
}
