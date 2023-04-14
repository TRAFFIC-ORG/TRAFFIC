using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System.IO;
public class TrainingControl : MonoBehaviour
{
    List<Simulation> sims;
    [SerializeField] GameObject simPrefab, generation;
    GameObject[] simsDisplayObject;
    SimDisplay[] simsDisplay;
    TextMeshProUGUI generationText;
    private int currentGeneration;
    void Start()
    {
        sims = new List<Simulation>();
        simsDisplayObject = new GameObject[20];
        simsDisplay = new SimDisplay[20];
        float currentX = 1;
        float currentY = 0.5f;
        int currentDisplay =0;
        for(int i=0; i<4; i++){
            for(int j=0; j<5; j++){
                sims.Add(new Simulation());
                Vector3 position = new Vector3(currentX,currentY,0);
                simsDisplayObject[currentDisplay] = Instantiate(simPrefab,position,Quaternion.identity,this.transform);
                simsDisplay[currentDisplay] = simsDisplayObject[currentDisplay].GetComponent<SimDisplay>();
                currentDisplay ++;
                currentX += 3;
            }
            currentX = 1;
            currentY -= 2.3f;
        }
        currentGeneration = 0;
        generationText = generation.GetComponent<TextMeshProUGUI>();
        StartCoroutine(trainNetwork());
    }
    void Update()
    {
        for(int i=0; i<sims.Count; i++){
            sims[i].addCars();
            sims[i].carControl();
            simsDisplay[i].setState(sims[i].getCurrentState());
            simsDisplay[i].setText(sims[i].getCars());
        }
        generationText.text = "Generation: "+currentGeneration;
    }
    public void train(){
        int topScore = sims[0].getScore();
        int topScoreIndex = 0;
        for(int i=0; i<sims.Count; i++){
            if(topScore > sims[i].getScore()){
                topScoreIndex = i;
                topScore = sims[i].getScore();
            }
        }
        Simulation topSim = sims[topScoreIndex];
        float[][] topWeights = topSim.getWeights();
        //Save top weights to a file
        sims.Clear();
        for(int x=0; x<18; x++){
            float[][] newWeights = topWeights;
            for(int i=0; i<topWeights.Length; i++){
                for(int j=0; j<topWeights[i].Length; j++){
                    topWeights[i][j] += Random.Range(-0.1f,0.11f);
                }
            }
            sims.Add(new Simulation(newWeights));
        }
        sims.Add(new Simulation());
        sims.Add(new Simulation());
        WriteString(weightsToString(topWeights));
        Debug.Log(weightsToString(topWeights));
    }
    public string weightsToString(float[][] weights){
        string savedWeights = "";
        for(int i=0; i<weights.Length; i++){
                for(int j=0; j<weights[i].Length; j++){
                    if(j!=0){
                        savedWeights += ","+weights[i][j];
                    }
                    else{
                        savedWeights += +weights[i][j];
                    }
                }
                if(i!=weights.Length-1){
                    savedWeights += ":";
                }
            }
        return savedWeights;
    }
    public static void WriteString(string weights)
    {
       string path = Application.persistentDataPath + "/weights.txt";
       File.WriteAllText(path, "");
       //Write some text to the test.txt file
       StreamWriter writer = new StreamWriter(path, true);
       writer.WriteLine(weights);
       writer.Close();
       StreamReader reader = new StreamReader(path);
       //Print the text from the file
       Debug.Log(reader.ReadToEnd());
       reader.Close();
    }
    public static void ReadString()
    {
        string path = Application.persistentDataPath + "/weights.txt";
        //Read the text from directly from the test.txt file
        StreamReader reader = new StreamReader(path);
        Debug.Log(reader.ReadToEnd());
        reader.Close();
    }
    IEnumerator trainNetwork(){
        while(true){
            yield return new WaitForSeconds(5f);
            train();
            currentGeneration ++;
        }
    }
}
