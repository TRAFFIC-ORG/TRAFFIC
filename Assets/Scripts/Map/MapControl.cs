using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using TMPro;
public class MapControl : MonoBehaviour
{
    private bool roadSelected;
    [SerializeField] GameObject intersectionPrefab, roadPrefab, nameInput;
    private List<GameObject> intersections;
    private List<GameObject> roads;
    private int currentIntersection;
    private GameObject[] selectedIntersection;
    private TMP_InputField nameInputText;
    // Start is called before the first frame update
    void Start()
    {
        intersections = new List<GameObject>();
        roads = new List<GameObject>();
        currentIntersection = 0;
        selectedIntersection = new GameObject[2];
        nameInputText = nameInput.GetComponent<TMP_InputField>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void goBack(){
        SceneManager.LoadScene(0);
    }
    public void setIntersection(GameObject newIntersection){
        if(roadSelected){
            selectedIntersection[currentIntersection] = newIntersection;
            if(currentIntersection == 1){
                //Spawn Road
                Vector3 roadPos = new Vector3(0,0,0);
                roads.Add(Instantiate(roadPrefab,roadPos,Quaternion.identity));
                LineRenderer currentLine = roads[roads.Count-1].GetComponent<LineRenderer>();
                currentLine.SetPosition(0,selectedIntersection[0].transform.position);
                currentLine.SetPosition(1,selectedIntersection[1].transform.position);
                currentIntersection = 0;
            }
            else{
                currentIntersection ++;
            }
        }
    }
    public void setRoad(bool newRoad){
        roadSelected = newRoad;
    }
    private void OnMouseDown() {
        Vector2 mousePostion = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        //Add intersection
        if(roadSelected == false){
            intersections.Add(Instantiate(intersectionPrefab,new Vector3(mousePostion.x,mousePostion.y,0),Quaternion.identity));
            intersections[intersections.Count-1].name = intersections.Count+"";
        }
    }
    public void saveMap(){
        List<string> mapStrings = new List<string>();
        string currentMap = nameInputText.text;
        if(currentMap == ""){
            Debug.Log("Please input a map name");
        }
        else{
            //Type:x,y
            for(int i=0; i<intersections.Count; i++){
                string currentIntersectionString = "I:";
                currentIntersectionString += intersections[i].transform.position.x + "," + intersections[i].transform.position.y;
                mapStrings.Add(currentIntersectionString);
            }
            //Type:x,y:x2,y2
            for(int i=0; i<roads.Count; i++){
                string currentRoadString = "R:";
                LineRenderer currentLine = roads[i].GetComponent<LineRenderer>();
                Vector3 point1 = currentLine.GetPosition(0);
                Vector3 point2 = currentLine.GetPosition(1);
                currentRoadString += point1.x + "," + point1.y + ":";
                currentRoadString += point2.x + "," + point2.y;
                mapStrings.Add(currentRoadString);
            }
            WriteString(mapStrings,currentMap);
            nameInputText.text = "";
        }
    }
    public void loadMap(){
        string currentMap = nameInputText.text;
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
                        roads.Add(Instantiate(roadPrefab,new Vector3(0,0,0),Quaternion.identity));
                        LineRenderer currentLine = roads[roads.Count-1].GetComponent<LineRenderer>();
                        currentLine.SetPosition(0,new Vector3(float.Parse(pos1[0]),float.Parse(pos1[1]),0));
                        currentLine.SetPosition(1,new Vector3(float.Parse(pos2[0]),float.Parse(pos2[1]),0));
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
    public static void WriteString(List<string> mapStrings, string selectedMap)
    {
        string folderPath = Application.persistentDataPath + "/Maps/";
        if (!Directory.Exists(folderPath)) {
            Directory.CreateDirectory(folderPath);
        }
       string path = folderPath + selectedMap + ".txt";
       Debug.Log(path);
       File.WriteAllText(path, "");
       //Write some text to the test.txt file
       StreamWriter writer = new StreamWriter(path, true);
       for(int i=0; i<mapStrings.Count; i++){
            writer.WriteLine(mapStrings[i]);
       }
       writer.Close();
       StreamReader reader = new StreamReader(path);
       reader.Close();
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
