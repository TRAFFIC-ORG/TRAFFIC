using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class StartScreenController : MonoBehaviour
{
    public void loadNewScene(int newScene){
        SceneManager.LoadScene(newScene);
    } 
}
