using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using TMPro;
public class SimControl : MonoBehaviour
{
    private int selection; //0=Debug, 1=Custom, 2=Generated
    [SerializeField]private GameObject[] holders;
    public void setSelection(int newSelection){
        this.selection = newSelection;
        holders[selection].SetActive(true);
        holders[2].SetActive(false);
    }
    public void goBack(){
        SceneManager.LoadScene(0);
    }
}
