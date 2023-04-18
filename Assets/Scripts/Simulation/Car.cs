using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{
    private Vector3 nextNode;
    [SerializeField] private GameObject simControll, currentGameControll;
    private SimControl mainControll;
    private Node startNode;
    private Node endNode;
    private Queue<Node> path;
    void Start()
    {
        mainControll = GameObject.Find("SimControl").GetComponent<SimControl>();
        List<GameObject> allNodes = mainControll.GetNodes();
        Debug.Log(allNodes.Count);
        startNode = allNodes[(int)Random.Range(0,allNodes.Count)].GetComponent<Node>();
        Debug.Log("Start-"+startNode.name);
        endNode = allNodes[(int)Random.Range(0,allNodes.Count)].GetComponent<Node>();
        Debug.Log("End-"+endNode.name);
        while(endNode == startNode){
            endNode = allNodes[(int)Random.Range(0,allNodes.Count)].GetComponent<Node>();
        }
        path = Dijkstra(startNode,endNode);
        Node[] pathArray = path.ToArray();
        for(int i=0; i<path.Count; i++){
            pathArray[i].GetComponent<SpriteRenderer>().color = Color.green;
        }
        startNode.GetComponent<SpriteRenderer>().color = Color.blue;
        endNode.GetComponent<SpriteRenderer>().color = Color.black;
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
            Debug.Log(currentNode.name);
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
