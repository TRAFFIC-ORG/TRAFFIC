using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{
    private Vector3 nextNode;
    [SerializeField] private GameObject simControll, currentGameControll;
    [SerializeField] private Sprite greenLight;
    private SimControl mainControll;
    private Node startNode;
    private Node endNode;
    private Queue<Node> path;
    private Node[] pathArray;
    private int nextNodeNumber;
    private int carSpeed = 1;
    private bool isEntering;
    private int enteringSide;
    private int exitingSide;
    private bool hasExited;
    private int previousSide;
    private bool inQue;
    void Start()
    {
        mainControll = GameObject.Find("SimControl").GetComponent<SimControl>();
        List<GameObject> allNodes = mainControll.GetNodes();
        startNode = allNodes[(int)Random.Range(0,allNodes.Count)].GetComponent<Node>();
        endNode = allNodes[(int)Random.Range(0,allNodes.Count)].GetComponent<Node>();
        while(endNode == startNode){
            endNode = allNodes[(int)Random.Range(0,allNodes.Count)].GetComponent<Node>();
        }
        path = Dijkstra(startNode,endNode);
        pathArray = path.ToArray();
        // for(int i=0; i<path.Count; i++){
        //     pathArray[i].GetComponent<SpriteRenderer>().color = Color.green;
        // }
        // startNode.GetComponent<SpriteRenderer>().color = Color.yellow;
        // endNode.GetComponent<SpriteRenderer>().color = Color.black;
        this.transform.position = startNode.transform.position;
        nextNodeNumber = 0;
        Quaternion targetRotation = Quaternion.LookRotation(Vector3.forward,-1*(pathArray[nextNodeNumber].transform.position - transform.position).normalized);
        this.transform.rotation = targetRotation;
        isEntering = false;
        exitingSide = -1;
        hasExited = false;
        inQue =false;
    }
    void Update(){
        if(inQue){

        }
        else{
            Vector3 direction = (pathArray[nextNodeNumber].transform.position - transform.position).normalized;
            if(exitingSide != -1){
                direction = (pathArray[nextNodeNumber].getSide(exitingSide).transform.position - transform.position).normalized;
            }
            transform.position += direction * carSpeed * Time.deltaTime;
        }
    }
    public void removeFromQue(){this.inQue = false;}
    private void OnTriggerEnter2D(Collider2D other) {
        if(other.tag == "Node"){
            if(other.GetComponent<Node>() == pathArray[nextNodeNumber]){
                if(other.GetComponent<Node>() == endNode){
                    Destroy(this.gameObject);
                }
                else{
                    //Get incoming, Determine heading, set position to correct section
                    this.transform.position = pathArray[nextNodeNumber].getSide(enteringSide).transform.position;
                    nextNodeNumber ++;
                    Quaternion targetRotation = Quaternion.LookRotation(Vector3.forward,-1*(pathArray[nextNodeNumber].transform.position - transform.position).normalized);
                    this.transform.rotation = targetRotation;
                }
            }
        }
        if(other.tag == "Light"){
            if(isEntering && hasExited == false){
                exitingSide = -1;
                int que = 0;
                enteringSide = int.Parse(other.transform.name);
                switch(enteringSide){
                    case 4:
                        enteringSide = 3;
                        que = 0;
                    break;

                    case 5:
                        enteringSide = 0;
                        que = 1;
                    break;

                    case 6:
                        enteringSide = 1;
                        que = 2;
                    break;

                    case 7:
                        enteringSide = 2;
                        que = 7;
                    break;
                }
                if(other.GetComponent<SpriteRenderer>().sprite == greenLight){
                    //Nothing
                }
                else{
                    inQue = true;
                    Debug.Log(inQue);
                    other.transform.parent.GetComponent<Node>().addToQue(que, this);
                }
            }
            else if(!isEntering && !hasExited){
                exitingSide = int.Parse(other.transform.name);
                switch(exitingSide){
                    case 4:
                        exitingSide = 1;
                        previousSide = 0;
                    break;

                    case 5:
                        exitingSide = 2;
                        previousSide = 1;
                    break;

                    case 6:
                        exitingSide = 3;
                        previousSide = 2;
                    break;

                    case 7:
                        exitingSide = 0;
                        previousSide = 3;
                    break;
                }
                if(mainControll.getSelection() == 0){
                    if(exitingSide == 1 || exitingSide ==3){
                        this.transform.position = new Vector3(pathArray[nextNodeNumber].getSide(exitingSide).transform.position.x,transform.position.y,0);
                    }
                    else{
                        this.transform.position = new Vector3(transform.position.x,pathArray[nextNodeNumber].getSide(exitingSide).transform.position.y,0);
                    }
                }
                else{
                    hasExited = true;
                    if(nextNodeNumber >= 1){
                        Debug.Log("test");
                        this.transform.position = pathArray[nextNodeNumber-1].getSide(previousSide).transform.position;
                    }
                    else{
                        this.transform.position = startNode.getSide(previousSide).transform.position;
                        Debug.Log("ol");
                    }
                }
                Quaternion targetRotation = Quaternion.LookRotation(Vector3.forward,-1*(pathArray[nextNodeNumber].getSide(exitingSide).transform.position - transform.position).normalized);
                this.transform.rotation = targetRotation;
            }
            if(hasExited){
                hasExited = false;
            }
            isEntering = !isEntering;
        }
    }
    Queue<Node> Dijkstra(Node start, Node goal)
    {
        Dictionary<Node, Node> nextNodeToGoal = new Dictionary<Node, Node>();
        Dictionary<Node, int> costToReachGoal = new Dictionary<Node, int>();
        
        PriorityQueue<Node> frontier = new PriorityQueue<Node>();
        frontier.Enqueue(goal, 0);
        costToReachGoal[goal] = 0;

        while (frontier.Count > 0)
        {
            Node currentNode = frontier.Dequeue();
            if (currentNode == start)
                break;
            List<Node> currentNodeNeighbors = currentNode.getNeighbors();
            foreach (Node neighbor in currentNodeNeighbors)
            {
                int newCost = costToReachGoal[currentNode] + neighbor.getCost();
                if (costToReachGoal.ContainsKey(neighbor) == false || newCost < costToReachGoal[neighbor])
                {
                    costToReachGoal[neighbor] = newCost;
                    int priority = newCost;
                    frontier.Enqueue(neighbor, priority);
                    nextNodeToGoal[neighbor] = currentNode;
                    neighbor.setText(costToReachGoal[neighbor].ToString());
                }
            }
        }
        if (nextNodeToGoal.ContainsKey(start) == false)
        {
            Debug.Log("Test");
            return null;
        }

        Queue<Node> path = new Queue<Node>();
        Node pathNode = start;
        while (goal != pathNode)
        {
            pathNode = nextNodeToGoal[pathNode];
            path.Enqueue(pathNode);
        }
        return path;
    }
}
