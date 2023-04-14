using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class MapControl : MonoBehaviour
{
    private bool roadSelected;
    [SerializeField] GameObject intersectionPrefab, roadPrefab;
    List<GameObject> intersections;
    List<GameObject> roads;
    private int currentIntersection;
    GameObject[] selectedIntersection;
    // Start is called before the first frame update
    void Start()
    {
        intersections = new List<GameObject>();
        roads = new List<GameObject>();
        currentIntersection = 0;
        selectedIntersection = new GameObject[2];
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void goBack(){
        SceneManager.LoadScene(0);
    }
    public void setIntersection(GameObject newIntersection){
        selectedIntersection[currentIntersection] = newIntersection;
        if(currentIntersection == 1){
            //Spawn Road
            Vector3 roadPos = new Vector3((selectedIntersection[1].transform.position.x+selectedIntersection[0].transform.position.x)/2,(selectedIntersection[1].transform.position.y+selectedIntersection[0].transform.position.y)/2, 0);
            roads.Add(Instantiate(roadPrefab,roadPos,Quaternion.identity));
            float xScale = Mathf.Sqrt(Mathf.Pow(selectedIntersection[1].transform.position.x-selectedIntersection[0].transform.position.x,2)+Mathf.Pow(selectedIntersection[1].transform.position.y-selectedIntersection[0].transform.position.y,2));
            roads[roads.Count-1].transform.localScale = new Vector3(xScale,0.1661665f,0);
            //Rotate the road
            float angle = Mathf.Atan(selectedIntersection[1].transform.position.y-selectedIntersection[0].transform.position.y/selectedIntersection[1].transform.position.x-selectedIntersection[0].transform.position.x);
            float angleDeg = angle * Mathf.Rad2Deg;
            Debug.Log(angleDeg);
            roads[roads.Count-1].transform.rotation = Quaternion.Euler(new Vector3(0,0,angleDeg/2));
            currentIntersection = 0;
        }
        else{
            currentIntersection ++;
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
}
