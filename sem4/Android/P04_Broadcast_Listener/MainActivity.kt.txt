package com.example.prac4a

import android.content.Context
import android.net.ConnectivityManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val c=applicationContext.getSystemService(Context.CONNECTIVITY_SERVICE)as ConnectivityManager

        val networkInfo=c.activeNetworkInfo
        if (networkInfo!=null && networkInfo.isConnected )
        {
            if(networkInfo.type==ConnectivityManager.TYPE_MOBILE)
            {
                Toast.makeText(this,"device connected to mobile data",Toast.LENGTH_LONG).show()
            }
            if(networkInfo.type==ConnectivityManager.TYPE_WIFI)
            {
                Toast.makeText(this,"device connected to mobile wifi",Toast.LENGTH_LONG).show()
            }
        }
        else
        {
            Toast.makeText(this,"you are offline",Toast.LENGTH_LONG).show()
        }




    }
}