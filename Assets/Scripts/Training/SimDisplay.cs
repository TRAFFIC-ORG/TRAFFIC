using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
public class SimDisplay : MonoBehaviour
{
    [SerializeField] GameObject[] lights; //NEWS
    [SerializeField] Sprite[] lightStateSprite;
    [SerializeField] GameObject[] numberDisplay;
    TextMeshPro[] numberDisplayText;
    // Start is called before the first frame update
    void Start()
    {
        numberDisplayText = new TextMeshPro[numberDisplay.Length];
        for(int i=0; i<numberDisplayText.Length; i++){
            numberDisplayText[i] = numberDisplay[i].GetComponent<TextMeshPro>();
        }
    }
    public void setText(int[] carsNumbers){
        for(int i=0; i<numberDisplayText.Length; i++){
            numberDisplayText[i].text = carsNumbers[i] + "";
        }
    }
    public void setState(int state){
        if(state == 1){
            lights[0].GetComponent<SpriteRenderer>().sprite = lightStateSprite[1];
            lights[1].GetComponent<SpriteRenderer>().sprite = lightStateSprite[0];
            lights[2].GetComponent<SpriteRenderer>().sprite = lightStateSprite[1];
            lights[3].GetComponent<SpriteRenderer>().sprite = lightStateSprite[0];
        }
        else{
            lights[0].GetComponent<SpriteRenderer>().sprite = lightStateSprite[0];
            lights[1].GetComponent<SpriteRenderer>().sprite = lightStateSprite[1];
            lights[2].GetComponent<SpriteRenderer>().sprite = lightStateSprite[0];
            lights[3].GetComponent<SpriteRenderer>().sprite = lightStateSprite[1];
        }
    }
}
