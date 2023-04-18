using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Node : MonoBehaviour
{
    [SerializeField] GameObject trafficLightPre, simController;
    [SerializeField] Sprite redLight, greenLight;
    [SerializeField] bool debugMode;
    private GameObject[] trafficLights;
    private SpriteRenderer[] trafficLightSprites;
    private SimControl controller;
    private int currentLightState; //1 is North/South, -1 is East/West
    private string text;
    private int cost;
    private List<Node> neighbors;
    private string[] neighborString;
    // Start is called before the first frame update
    void Start()
    {
        simController = GameObject.Find("SimControl");
        currentLightState = 1;
        controller = simController.GetComponent<SimControl>();
        trafficLights = new GameObject[4];
        trafficLightSprites = new SpriteRenderer[4];

        trafficLights[0] = Instantiate(trafficLightPre, new Vector3(this.transform.position.x,this.transform.position.y+0.3f,0), Quaternion.identity,this.transform);
        trafficLights[1] = Instantiate(trafficLightPre, new Vector3(this.transform.position.x+0.25f,this.transform.position.y,0), Quaternion.identity,this.transform);
        trafficLights[2] = Instantiate(trafficLightPre, new Vector3(this.transform.position.x,this.transform.position.y-0.3f,0), Quaternion.identity,this.transform);
        trafficLights[3] = Instantiate(trafficLightPre, new Vector3(this.transform.position.x-0.25f,this.transform.position.y,0), Quaternion.identity,this.transform);

        for(int i=0; i<trafficLights.Length; i++){
            trafficLightSprites[i] = trafficLights[i].GetComponent<SpriteRenderer>();
        }
        if(debugMode){
            StartCoroutine(DebugLightMode());
        }
        else{
            StartCoroutine(AILightMode());
        }
        cost = 1;
    }
    public int getCost(){return cost;}
    public void setText(string text){this.text = text;}
    public string getText(){return this.text;}
    public void setNeighborString(string[] neighborString){
        this.neighborString = neighborString;
    }
    public void findNeighbors(){
        neighbors = new List<Node>();
        for(int i=0; i<neighborString.Length; i++){
            neighbors.Add(this.transform.parent.GetChild(int.Parse(neighborString[i])).GetComponent<Node>());
        }
    }   
    IEnumerator AILightMode(){
        while(true){
            float[] testArray = new float[4]{(int)Random.Range(0,5),(int)Random.Range(0,5),(int)Random.Range(0,5),(int)Random.Range(0,5)};
            currentLightState *= controller.getBrainOutput(testArray);
            switch(currentLightState){
                case -1:
                trafficLightSprites[0].sprite = redLight;
                trafficLightSprites[1].sprite = greenLight;
                trafficLightSprites[2].sprite = redLight;
                trafficLightSprites[3].sprite = greenLight;
                break;

                case 1:
                trafficLightSprites[0].sprite = greenLight;
                trafficLightSprites[1].sprite = redLight;
                trafficLightSprites[2].sprite = greenLight;
                trafficLightSprites[3].sprite = redLight;
                break;
            }
            yield return new WaitForSeconds(2);
        }
    }
    IEnumerator DebugLightMode(){
        while(true){
            currentLightState *= -1;
            switch(currentLightState){
                case -1:
                trafficLightSprites[0].sprite = redLight;
                trafficLightSprites[1].sprite = greenLight;
                trafficLightSprites[2].sprite = redLight;
                trafficLightSprites[3].sprite = greenLight;
                break;

                case 1:
                trafficLightSprites[0].sprite = greenLight;
                trafficLightSprites[1].sprite = redLight;
                trafficLightSprites[2].sprite = greenLight;
                trafficLightSprites[3].sprite = redLight;
                break;
            }
            yield return new WaitForSeconds(5);
        }
    }
    public void setNeighbors(List<Node> neighbors){
        this.neighbors = neighbors;
    }
    public List<Node> getNeighbors(){
        return neighbors;
    }
}
