package com.example.calc

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var num1:EditText
    private lateinit var num2:EditText
    private lateinit var add:Button
    private lateinit var sub:Button
    private lateinit var mul:Button
    private lateinit var divi:Button
    private lateinit var t1:TextView
    private lateinit var t2:TextView
    private lateinit var t3:TextView
    private lateinit var t4:TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        num1=findViewById(R.id.num1)
        num2=findViewById(R.id.num2)
        add=findViewById(R.id.add)
        sub=findViewById(R.id.sub)
        mul=findViewById(R.id.mul)
        divi=findViewById(R.id.divi)
        t1=findViewById(R.id.t1)
        t2=findViewById(R.id.t2)
        t3=findViewById(R.id.t3)
        t4=findViewById(R.id.t4)

        add.setOnClickListener{
            val n1=num1.text.toString().toDouble()
            val n2=num2.text.toString().toDouble()
            val show1=n1+n2
            t1.text=java.lang.Double.toString(show1)
        }
        sub.setOnClickListener{
            val n1=num1.text.toString().toDouble()
            val n2=num2.text.toString().toDouble()
            val show2=n1-n2
            t2.text=java.lang.Double.toString(show2)
        }
        mul.setOnClickListener{
            val n1=num1.text.toString().toDouble()
            val n2=num2.text.toString().toDouble()
            val show3=n1*n2
            t3.text=java.lang.Double.toString(show3)
        }
        divi.setOnClickListener{
            val n1=num1.text.toString().toDouble()
            val n2=num2.text.toString().toDouble()
            val show=n1/n2
            t4.text=java.lang.Double.toString(show)
        }
    }
}