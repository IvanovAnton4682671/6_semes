package com.example.information_about_student

import android.app.Activity
import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

const val ALL_TAGS = "com.example.information_about_student.all_tags"
const val ALL_CONTENT = "com.example.information_about_student.all_content"

class InformationActivity : AppCompatActivity() {

    private lateinit var etSurname: EditText
    private lateinit var etName: EditText
    private lateinit var etPatronymic: EditText
    private lateinit var etDateOfBirth: EditText
    private lateinit var etFaculty: EditText
    private lateinit var etCourse: EditText
    private lateinit var etGroup: EditText
    private lateinit var etPhone: EditText
    private lateinit var btnSaveInformation: Button
    private lateinit var btnCancel: Button
    private lateinit var btnClear: Button

    companion object {
        fun newIntent(packagesContext: Context, wrapContentIn: ArrayList<String>): Intent {
            return Intent(packagesContext, InformationActivity::class.java).apply {
                putStringArrayListExtra(ALL_CONTENT, wrapContentIn)
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_information)

        etSurname = findViewById(R.id.etSurname)
        etName = findViewById(R.id.etName)
        etPatronymic = findViewById(R.id.etPatronymic)
        etDateOfBirth = findViewById(R.id.etDateOfBirth)
        etFaculty = findViewById(R.id.etFaculty)
        etCourse = findViewById(R.id.etCourse)
        etGroup = findViewById(R.id.etGroup)
        etPhone = findViewById(R.id.etPhone)
        btnSaveInformation = findViewById(R.id.btnSaveInformation)
        btnCancel = findViewById(R.id.btnCancel)
        btnClear = findViewById(R.id.btnClear)

        val wrapContentIn = intent.getStringArrayListExtra(ALL_CONTENT)
        val wrapAllEdTt = arrayListOf<EditText>(etSurname, etName, etPatronymic, etDateOfBirth, etFaculty, etCourse, etGroup, etPhone)
        if (wrapContentIn != null) {
            for (i in 0..(wrapContentIn.count() - 1)) {
                wrapAllEdTt[i].append(wrapContentIn.get(i) ?: "")
            }
        }

        btnSaveInformation.setOnClickListener {
            val textSurname = etSurname.text.toString()
            val textName = etName.text.toString()
            val textPatronymic = etPatronymic.text.toString()
            val textDateOfBirth = etDateOfBirth.text.toString()
            val textFaculty = etFaculty.text.toString()
            val textCourse = etCourse.text.toString()
            val textGroup = etGroup.text.toString()
            val textPhone = etPhone.text.toString()
            var flag: Int = 0


            if (textPhone.isBlank()) {
                setError(etPhone, "Введите номер телефона!")
                flag += 1
            }
            else if (!(Regex("^[0-9]{11}").matches(textPhone))) {
                setError(etPhone, "Введите номер телефона в корректном виде (пример: 89181214590)!")
                flag += 1
            }
            if (textGroup.isBlank()) {
                setError(etGroup, "Введите группу!")
                flag += 1
            }
            else if (!(Regex("^[a-zA-Zа-яА-Я0-9\\s/,]{2,50}").matches(textGroup))) {
                setError(etGroup, "Введите группу в корректном виде (рус./англ. буквы, цифры, пробел и '/', от 2 до 50 символов)!")
                flag += 1
            }
            if (textCourse.isBlank()) {
                setError(etCourse, "Введите курс!")
                flag += 1
            }
            else if (!(Regex("^[1-6]{1}\$").matches(textCourse))) {
                setError(etCourse, "Введите курс в корректном виде (цифра от 1 до 6)!")
                flag += 1
            }
            if (textFaculty.isBlank()) {
                setError(etFaculty, "Введите факультет!")
                flag += 1
            }
            else if (!(Regex("^[a-zA-Zа-яА-Я\\s-]{3,100}\$").matches(textFaculty))) {
                setError(etFaculty, "Введите факультет в корректном виде (рус./англ. язык, только буквы, от 3 до 100 символов)!")
                flag += 1
            }
            if (textDateOfBirth.isBlank()) {
                setError(etDateOfBirth, "Введите дату рождения!")
                flag += 1
            }
            else {
                val dateRegex = Regex("^(0?[1-9]|[12][0-9]|3[01])\\.(0?[1-9]|1[0-2])\\.(1?\\d{1,3}|200\\d|201[0-9]|202[0-4])\$")
                if (dateRegex.matches(textDateOfBirth)) {
                    val dateParts = textDateOfBirth.split(".")
                    val day = dateParts[0].toInt()
                    val month = dateParts[1].toInt()
                    val year = dateParts[2].toInt()
                    val maxDaysInMonth = when (month) {
                        1, 3, 5, 7, 8, 10, 12 -> 31
                        4, 6, 9, 11 -> 30
                        2 -> if (year % 4 == 0) 29 else 28
                        else -> 0
                    }
                    if (day > maxDaysInMonth) {
                        setError(etDateOfBirth, "Введённый день не соответствует выбранному месяцу!")
                        flag += 1
                    }
                } else {
                    setError(etDateOfBirth, "Введите дату в корректном виде (как пример: 08.02.2003)!")
                    flag += 1
                }
            }
            if (textPatronymic.isBlank()) {
                setError(etPatronymic, "Введите отчество!")
                flag += 1
            }
            else if (!(Regex("^[A-ZА-Я]{1}[a-zA-Zа-яА-Я-]{1,49}\$").matches(textPatronymic))) {
                setError(etPatronymic, "Введите отчество в корректном виде (рус./англ. язык, первая буква заглавная, остальные строчные, символ '-', до 50 символов)!")
                flag += 1
            }
            if (textName.isBlank()) {
                setError(etName, "Введите имя!")
                flag += 1
            }
            else if (!(Regex("^[A-ZА-Я]{1}[a-zA-Zа-яА-Я-]{1,49}\$").matches(textName))) {
                setError(etName, "Введите имя в корректном виде (рус./англ. язык, первая буква заглавная, остальные строчные, символ '-', до 50 символов)!")
                flag += 1
            }
            if (textSurname.isBlank()) {
                setError(etSurname, "Введите фамилию!")
                flag += 1
            }
            else if (!(Regex("^[A-ZА-Я]{1}[a-zA-Zа-яА-Я-]{1,49}\$").matches(textSurname))) {
                setError(etSurname, "Введите фамилию в корректном виде (рус./англ. язык, первая буква заглавная, остальные строчные, символ '-', до 50 символов)!")
                flag += 1
            }
            if (flag == 0) {
                val wrapTags = arrayListOf<String>("Фамилия", "Имя", "Отчество", "Дата рождения", "Факультет", "Курс", "Группа", "Телефон")
                val wrapContent = arrayListOf<String>(textSurname, textName, textPatronymic, textDateOfBirth, textFaculty, textCourse, textGroup, textPhone)
                intent.putExtra(ALL_TAGS, wrapTags)
                intent.putExtra(ALL_CONTENT, wrapContent)
                setResult(Activity.RESULT_OK, intent)
                finish()
            }
        }

        btnCancel.setOnClickListener {
            val wrapTags = arrayListOf<String>()
            val wrapContent = arrayListOf<String>()
            intent.putExtra(ALL_TAGS, wrapTags)
            intent.putExtra(ALL_CONTENT, wrapContent)
            setResult(Activity.RESULT_OK, intent)
            finish()
        }

        btnClear.setOnClickListener {
            val wrapAllET = arrayListOf<EditText>(etSurname, etName, etPatronymic, etDateOfBirth, etFaculty, etCourse, etGroup, etPhone)
            for (i in 0..(wrapAllET.count() - 1)) {
                wrapAllET[i].setText("")
            }
        }
    }

    private fun setError(editText: EditText, slogan: String) {
        editText.error = slogan
        editText.requestFocus()
    }
}