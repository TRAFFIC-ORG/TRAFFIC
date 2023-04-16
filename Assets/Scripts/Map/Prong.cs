using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class Prong : MonoBehaviour
{
    [SerializeField] GameObject control;
    MapControl map;
    // Start is called before the first frame update
    void Start()
    {
        if(SceneManager.GetActiveScene().buildIndex == 1){
            map = GameObject.Find("MapControl").GetComponent<MapControl>();
        }
    }
    private void OnMouseDown() {
        Debug.Log("works");
        map.setIntersection(this.gameObject);
    }
}
