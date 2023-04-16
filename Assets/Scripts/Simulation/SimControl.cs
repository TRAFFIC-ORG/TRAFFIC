using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using TMPro;
public class SimControl : MonoBehaviour
{
    private int selection; //0=Debug, 1=Custom, 2=Generated
    private Brain network;
    private float[][] weights;
    [SerializeField]private GameObject[] holders;
    [SerializeField] private GameObject nameInput;
    private TMP_InputField nameInputText;
    private string mapName;
    private void Start() {
        loadWeights();
        network = new Brain(weights);
        nameInputText = nameInput.GetComponent<TMP_InputField>();
    }
    public void setSelection(int newSelection){
        this.selection = newSelection;
        holders[selection].SetActive(true);
        holders[2].SetActive(false);
        mapName = nameInputText.text;
    }
    public int getSelection(){
        return selection;
    }
    public string getMapName(){
        return mapName;
    }
    public void goBack(){
        SceneManager.LoadScene(0);
    }
    public void loadWeights(){
        List<string> mapStrings = new List<string>();
        string path = Application.persistentDataPath + "/weights.txt";
        if(File.Exists(path)){
            StreamReader reader = new StreamReader(path);
            string wholeBrain = reader.ReadToEnd();
            string[] perceptrons = wholeBrain.Split(":");
            weights = new float[perceptrons.Length][];
            for(int i=0; i<perceptrons.Length; i++){
                string[] storedWeights = perceptrons[i].Split(",");
                weights[i] = new float[storedWeights.Length];
                for(int x=0; x<storedWeights.Length; x++){
                    weights[i][x] = float.Parse(storedWeights[x]);
                }
            }
            reader.Close();
        }
    }
    public int getBrainOutput(float[] inputs){
        return network.chooseState(inputs);
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
}
