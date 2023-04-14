using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Intersection : MonoBehaviour
{
    [SerializeField] GameObject control;
    MapControl map;
    // Start is called before the first frame update
    void Start()
    {
        map = GameObject.Find("MapControl").GetComponent<MapControl>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnMouseDown() {
        map.setIntersection(this.gameObject);
    }
}
