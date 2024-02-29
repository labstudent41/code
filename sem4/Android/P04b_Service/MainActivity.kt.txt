package com.example.prac4b

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.example.prac4b.R.*



class MainActivity : AppCompatActivity() {

    private lateinit var btstop:Button
    private lateinit var btstart:Button


    override fun onCreate(savedInstanceState: Bundle?) {


        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btstop=findViewById(R.id.btstop)
        btstart=findViewById(R.id.btstart)


        btstart.setOnClickListener(){
            startService(Intent(this,NewService::class.java))
        }

        btstop.setOnClickListener(){
            stopService(Intent(this,NewService::class.java))
        }
    }
}