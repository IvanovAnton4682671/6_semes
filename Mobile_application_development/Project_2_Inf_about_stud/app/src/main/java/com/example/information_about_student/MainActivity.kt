package com.example.information_about_student

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.drm.DrmStore.Action
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.result.contract.ActivityResultContracts
import androidx.lifecycle.ViewModelProvider

class MainActivity : AppCompatActivity() {

    private lateinit var tvMain: TextView
    private lateinit var btnAddInformation: Button

    private val studentInformationViewModel: StudentInformationViewModel by lazy {
        val provider = ViewModelProvider(this)
        provider.get(StudentInformationViewModel::class.java)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        tvMain = findViewById(R.id.tvMain)
        btnAddInformation = findViewById(R.id.btnAddInformation)

        val resultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) {
            result ->
            if (result.resultCode == Activity.RESULT_OK) {
                val data: Intent? = result.data
                val wrapTags = data?.getStringArrayListExtra(ALL_TAGS)!!
                val wrapContentIn = data?.getStringArrayListExtra(ALL_CONTENT)!!
                if (wrapContentIn.isNotEmpty()) {
                    studentInformationViewModel.wrapContentIn = wrapContentIn
                }
                var text = "Информация о студенте\n"
                if (wrapTags.isNotEmpty() && wrapContentIn.isNotEmpty()) {
                    for (i in 0..(wrapTags.count() - 1))
                        text += "${wrapTags[i]}: ${wrapContentIn[i]}\n"
                    tvMain.visibility = View.VISIBLE
                    tvMain.setText(text)
                    studentInformationViewModel.studentInformation = text
                }
            }
        }

        tvMain.visibility = View.GONE

        btnAddInformation.setOnClickListener {
            val intent = InformationActivity.newIntent(this@MainActivity, studentInformationViewModel.wrapContentIn)
            resultLauncher.launch(intent)
        }
    }

    override fun onResume() {
        super.onResume()

        if (studentInformationViewModel.studentInformation.isNotEmpty()) {
            tvMain.visibility = View.VISIBLE
            tvMain.setText(studentInformationViewModel.studentInformation)
        }
        else {
            tvMain.visibility = View.GONE
        }
    }
}