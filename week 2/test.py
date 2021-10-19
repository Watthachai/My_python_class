using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    // float = จำนวน
    public int number ;
    // bool = ทศนิยม
    public float number_1;
    // bool = ถูกกับผิด
    public bool check;
    // bool = ตัวหนังสือ
    public string Text;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log(number);
    }

    // Update is called once per frame
    void Update()
    {
        if (80 <= number && number <= 100)
        {
            Debug.log("A");

        }
        else if(77 <= number && number < 80)
        {
            Debug.log("B+");
        }
        else if(70 <= number && number < 77)
        {
            Debug.log("B");
        }
        else if(67 <= number && number < 70)
        {
            Debug.log("C+");
        }
        else if(60 <= number && number < 67)
        {
            Debug.log("C");
        }
        else if(57 <= number && number < 60)
        {
            Debug.log("D+");
        }
        else if(50 <= number && number < 57)
        {
            Debug.log("D);
        }
        else if (0 <= number && number < 50)
        {
            Debug.log("F");
        }
    }

    void OnTriggerEnter(Collider other)
    {
        Destroy(gameObject);
    }

}