using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Node : MonoBehaviour
{
    [SerializeField] GameObject trafficLightPre;
    [SerializeField] Sprite redLight, greenLight;
    [SerializeField] bool debugMode;
    private GameObject[] trafficLights;
    private SpriteRenderer[] trafficLightSprites;
    private int currentLightState; //1 is North/South, -1 is East/West
    // Start is called before the first frame update
    void Start()
    {
        currentLightState = 1;
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
    }

    // Update is called once per frame
    void Update()
    {
        
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
}
