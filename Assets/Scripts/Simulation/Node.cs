using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Node : MonoBehaviour
{
    [SerializeField] GameObject trafficLightPre, simController;
    [SerializeField] Sprite redLight, greenLight;
    [SerializeField] bool debugMode;
    [SerializeField] private GameObject[] sections; //NE,SE,SW,NW
    private GameObject[] trafficLights;
    private SpriteRenderer[] trafficLightSprites;
    private SimControl controller;
    private int currentLightState; //1 is North/South, -1 is East/West
    private string text;
    private int cost;
    private List<Node> neighbors;
    private List<Car> carsWaitingNorth;
    private List<Car> carsWaitingEast;
    private List<Car> carsWaitingSouth;
    private List<Car> carsWaitingWest;
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

        carsWaitingNorth = new List<Car>();
        carsWaitingEast = new List<Car>();
        carsWaitingSouth = new List<Car>();
        carsWaitingWest = new List<Car>();

        for(int i=0; i<trafficLights.Length; i++){
            trafficLightSprites[i] = trafficLights[i].GetComponent<SpriteRenderer>();
            trafficLightSprites[i].name = i+4+"";
        }
        if(debugMode){
            StartCoroutine(DebugLightMode());
        }
        else{
            StartCoroutine(AILightMode());
        }
        cost = 1;
    }
    public void addToQue(int que, Car carInQue){
        switch(que){
            case 0:
            carsWaitingNorth.Add(carInQue);
            break;

            case 1:
            carsWaitingEast.Add(carInQue);
            break;

            case 2:
            carsWaitingSouth.Add(carInQue);
            break;

            case 3:
            carsWaitingWest.Add(carInQue);
            break;
        }
    }
    public GameObject getSide(int side){return sections[side];}
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
            float[] input = new float[4]{carsWaitingNorth.Count, carsWaitingEast.Count, carsWaitingSouth.Count, carsWaitingWest.Count};
            currentLightState *= controller.getBrainOutput(input);
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
            removeLight();
            yield return new WaitForSeconds(2);
        }
    }
    public void removeLight(){
        for(int i=0; i<2; i++){
                if(currentLightState == -1){
                    if(carsWaitingEast.Count > 0){
                        carsWaitingEast[0].removeFromQue();
                        carsWaitingEast.RemoveAt(0);
                    }
                    if(carsWaitingWest.Count > 0){
                        carsWaitingWest[0].removeFromQue();
                        carsWaitingWest.RemoveAt(0);
                    }
                }
                else{
                    if(carsWaitingNorth.Count > 0){
                        carsWaitingNorth[0].removeFromQue();
                        carsWaitingNorth.RemoveAt(0);
                    }
                    if(carsWaitingSouth.Count > 0){
                        carsWaitingSouth[0].removeFromQue();
                        carsWaitingSouth.RemoveAt(0);
                    }
                }
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
            removeLight();
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
