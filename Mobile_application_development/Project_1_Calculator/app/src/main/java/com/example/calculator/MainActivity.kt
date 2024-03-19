package com.example.calculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val etMain: EditText = findViewById(R.id.etMain)
        val tvOperation: TextView = findViewById(R.id.tvOperation)
        val tvAdditional: TextView = findViewById(R.id.tvAdditional)

        val btnClear: Button = findViewById(R.id.buttonClear)
        btnClear.setOnClickListener {
            etMain.setText("")
            tvOperation.setText("")
            tvAdditional.setText("")
            etMain.error = null
        }
        val btnDelete: Button = findViewById(R.id.buttonDelete)
        btnDelete.setOnClickListener {
            val textMain = etMain.text.toString()
            if (!(textMain.isBlank())) {
                etMain.setText(textMain.dropLast(1))
            }
        }

        val btn0: Button = findViewById(R.id.button0)
        btn0.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "0")
        }
        val btn1: Button = findViewById(R.id.button1)
        btn1.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "1")
        }
        val btn2: Button = findViewById(R.id.button2)
        btn2.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "2")
        }
        val btn3: Button = findViewById(R.id.button3)
        btn3.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "3")
        }
        val btn4: Button = findViewById(R.id.button4)
        btn4.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "4")
        }
        val btn5: Button = findViewById(R.id.button5)
        btn5.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "5")
        }
        val btn6: Button = findViewById(R.id.button6)
        btn6.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "6")
        }
        val btn7: Button = findViewById(R.id.button7)
        btn7.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "7")
        }
        val btn8: Button = findViewById(R.id.button8)
        btn8.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "8")
        }
        val btn9: Button = findViewById(R.id.button9)
        btn9.setOnClickListener {
            val text = etMain.text.toString()
            etMain.setText(text + "9")
        }

        val btnPoint: Button = findViewById(R.id.buttonPoint)
        btnPoint.setOnClickListener {
            val textMain = etMain.text.toString()
            if (!(textMain.isBlank()) && !('.' in textMain) && (textMain != "-")) {
                etMain.setText(textMain + ".")
            }
        }

        val btnEqual: Button = findViewById(R.id.buttonEqual)
        btnEqual.setOnClickListener {
            val textMain = etMain.text.toString()
            val textOperation = tvOperation.text.toString()
            val textAdditional = tvAdditional.text.toString()
            if (textMain.isNotEmpty() && textOperation.isNotEmpty() && textAdditional.isNotEmpty() && (textMain != "-")) {
                val num1 = textAdditional.toFloat()
                val num2 = textMain.toFloat()
                val answer = when(textOperation) {
                    "+" -> (num1 + num2).toString()
                    "-" -> (num1 - num2).toString()
                    "*" -> (num1 * num2).toString()
                    "/" -> if (num2.toInt() == 0) {
                        etMain.error = "Деление на ноль!"
                        return@setOnClickListener
                    }
                    else {
                        (num1 / num2).toString()
                    }
                    else -> ("").toString()
                }
                etMain.setText(answer)
                tvOperation.setText("")
                tvAdditional.setText("")
                etMain.error = null
            }
            else if ((textMain.isBlank() || textMain == "-") && textOperation.isBlank() && textAdditional.isBlank()) {
                etMain.error = "Введите число!"
                etMain.requestFocus()
            }
            else if ((textMain.isNotEmpty() && textOperation.isBlank()) or (textAdditional.isNotEmpty() && textOperation.isBlank())) {
                etMain.error = "Введите операцию!"
                etMain.requestFocus()
            }
            else if ((textAdditional.isNotEmpty() && textOperation.isNotEmpty() && textMain.isBlank()) or
                (textAdditional.isNotEmpty() && textOperation.isNotEmpty() && textMain == "-")) {
                etMain.error = "Введите второе число!"
                etMain.requestFocus()
            }
        }

        val btnPlus: Button = findViewById(R.id.buttonPlus)
        btnPlus.setOnClickListener {
            val textMain = etMain.text.toString()
            val textOperation = tvOperation.text.toString()
            val textAdditional = tvAdditional.text.toString()
            if (!("+-*/" in textOperation)) {
                if ((textMain.isBlank() || textMain == "-") && textOperation.isBlank() && textAdditional.isBlank()) {
                    etMain.error = "Введите число!"
                    etMain.requestFocus()
                }
                else if (!(textMain.isBlank()) && textOperation.isBlank() && textAdditional.isBlank() && textMain != "-") {
                    tvAdditional.setText(textMain)
                    tvOperation.setText("+")
                    etMain.setText("")
                    etMain.error = null
                }
                else if ((textMain.isBlank() && textOperation.isBlank() && !(textAdditional.isBlank())) or
                    ((textMain.isBlank() && !(textOperation.isBlank()) && !(textAdditional.isBlank())))) {
                    tvOperation.setText("+")
                    etMain.setText("")
                    etMain.error = null
                }
                else if (!(textAdditional.isBlank()) && !(textOperation.isBlank()) && (textMain == "-")) {
                    tvOperation.setText("+")
                    etMain.setText("")
                    etMain.error = null
                }
                else if (!(textMain.isBlank()) && !(textOperation.isBlank()) && !(textAdditional.isBlank()) && (textMain != "-")) {
                    val num1 = textAdditional.toFloat()
                    val num2 = textMain.toFloat()
                    val answer = when(textOperation) {
                        "+" -> (num1 + num2).toString()
                        "-" -> (num1 - num2).toString()
                        "*" -> (num1 * num2).toString()
                        "/" -> if (num2.toInt() == 0) {
                            etMain.error = "Деление на ноль!"
                            return@setOnClickListener
                        }
                        else {
                            (num1 / num2).toString()
                        }
                        else -> ("").toString()
                    }
                    tvAdditional.setText(answer)
                    tvOperation.setText("+")
                    etMain.setText("")
                    etMain.error = null
                }
            }
        }
        val btnMinus: Button = findViewById(R.id.buttonMinus)
        btnMinus.setOnClickListener {
            val textMain = etMain.text.toString()
            val textOperation = tvOperation.text.toString()
            val textAdditional = tvAdditional.text.toString()
            if ((textMain.isBlank() && textOperation.isBlank() && textAdditional.isBlank()) or
                (textMain.isBlank() && !(textOperation.isBlank()) && !(textAdditional.isBlank()) &&
                        (textOperation == "*" || textOperation == "/"))) {
                etMain.setText("-")
            }
            else if (!(textMain.isBlank()) && textOperation.isBlank() && textAdditional.isBlank() && (textMain != "-")) {
                tvAdditional.setText(textMain)
                tvOperation.setText("-")
                etMain.setText("")
            }
            else if ((textMain.isBlank() && textOperation.isBlank() && !(textAdditional.isBlank())) or
                (!(textMain.isBlank()) && (textMain == "-") && !(textOperation.isBlank()) && !(textAdditional.isBlank()))) {
                tvOperation.setText("-")
                etMain.setText("")
            }
            else if (textMain.isBlank() && !(textOperation.isBlank()) && !(textAdditional.isBlank())) {
                tvOperation.setText("-")
            }
            else if (!(textMain.isBlank()) && !(textOperation.isBlank()) && !(textAdditional.isBlank()) && (textMain != "-")) {
                val num1 = textAdditional.toFloat()
                val num2 = textMain.toFloat()
                val answer = when(textOperation) {
                    "+" -> (num1 + num2).toString()
                    "-" -> (num1 - num2).toString()
                    "*" -> (num1 * num2).toString()
                    "/" -> if (num2.toInt() == 0) {
                        etMain.error = "Деление на ноль!"
                        return@setOnClickListener
                    }
                    else {
                        (num1 / num2).toString()
                    }
                    else -> ("").toString()
                }
                tvAdditional.setText(answer)
                tvOperation.setText("-")
                etMain.setText("")
            }
        }
        val btnMultiply: Button = findViewById(R.id.buttonMultiply)
        btnMultiply.setOnClickListener {
            val textMain = etMain.text.toString()
            val textOperation = tvOperation.text.toString()
            val textAdditional = tvAdditional.text.toString()
            if (!("+-*/" in textOperation)) {
                if ((textMain.isBlank() || textMain == "-") && textOperation.isBlank() && textAdditional.isBlank()) {
                    etMain.error = "Введите число!"
                    etMain.requestFocus()
                }
                else if (!(textMain.isBlank()) && textOperation.isBlank() && textAdditional.isBlank() && textMain != "-") {
                    tvAdditional.setText(textMain)
                    tvOperation.setText("*")
                    etMain.setText("")
                    etMain.error = null
                }
                else if ((textMain.isBlank() && textOperation.isBlank() && !(textAdditional.isBlank())) or
                    ((textMain.isBlank() && !(textOperation.isBlank()) && !(textAdditional.isBlank())))) {
                    tvOperation.setText("*")
                    etMain.setText("")
                    etMain.error = null
                }
                else if (!(textAdditional.isBlank()) && !(textOperation.isBlank()) && (textMain == "-")) {
                    tvOperation.setText("*")
                    etMain.setText("")
                    etMain.error = null
                }
                else if (!(textMain.isBlank()) && !(textOperation.isBlank()) && !(textAdditional.isBlank()) && (textMain != "-")) {
                    val num1 = textAdditional.toFloat()
                    val num2 = textMain.toFloat()
                    val answer = when(textOperation) {
                        "+" -> (num1 + num2).toString()
                        "-" -> (num1 - num2).toString()
                        "*" -> (num1 * num2).toString()
                        "/" -> if (num2.toInt() == 0) {
                            etMain.error = "Деление на ноль!"
                            return@setOnClickListener
                        }
                        else {
                            (num1 / num2).toString()
                        }
                        else -> ("").toString()
                    }
                    tvAdditional.setText(answer)
                    tvOperation.setText("*")
                    etMain.setText("")
                    etMain.error = null
                }
            }
        }
        val btnDivide: Button = findViewById(R.id.buttonDivide)
        btnDivide.setOnClickListener {
            val textMain = etMain.text.toString()
            val textOperation = tvOperation.text.toString()
            val textAdditional = tvAdditional.text.toString()
            if (!("+-*/" in textOperation)) {
                if ((textMain.isBlank() || textMain == "-") && textOperation.isBlank() && textAdditional.isBlank()) {
                    etMain.error = "Введите число!"
                    etMain.requestFocus()
                }
                else if (!(textMain.isBlank()) && textOperation.isBlank() && textAdditional.isBlank() && textMain != "-") {
                    tvAdditional.setText(textMain)
                    tvOperation.setText("/")
                    etMain.setText("")
                    etMain.error = null
                }
                else if ((textMain.isBlank() && textOperation.isBlank() && !(textAdditional.isBlank())) or
                    ((textMain.isBlank() && !(textOperation.isBlank()) && !(textAdditional.isBlank())))) {
                    tvOperation.setText("/")
                    etMain.setText("")
                    etMain.error = null
                }
                else if (!(textAdditional.isBlank()) && !(textOperation.isBlank()) && (textMain == "-")) {
                    tvOperation.setText("/")
                    etMain.setText("")
                    etMain.error = null
                }
                else if (!(textMain.isBlank()) && !(textOperation.isBlank()) && !(textAdditional.isBlank()) && (textMain != "-")) {
                    val num1 = textAdditional.toFloat()
                    val num2 = textMain.toFloat()
                    val answer = when(textOperation) {
                        "+" -> (num1 + num2).toString()
                        "-" -> (num1 - num2).toString()
                        "*" -> (num1 * num2).toString()
                        "/" -> if (num2.toInt() == 0) {
                            etMain.error = "Деление на ноль!"
                            return@setOnClickListener
                        }
                        else {
                            (num1 / num2).toString()
                        }
                        else -> ("").toString()
                    }
                    tvAdditional.setText(answer)
                    tvOperation.setText("/")
                    etMain.setText("")
                    etMain.error = null
                }
            }
        }
    }
}