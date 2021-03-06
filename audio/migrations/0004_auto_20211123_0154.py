# Generated by Django 3.2.7 on 2021-11-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_alter_audio_categroty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='categroty',
            field=models.CharField(choices=[('عام', 'عام'), ('جذور-قرآنية', 'جذور-قرآنية'), ('ماذا-أتعلم-وكيف-أتعلم', 'ماذا-أتعلم-وكيف-أتعلم'), ('تأسيس-وعي-مسلم-معاصر-2', 'تأسيس-وعي-مسلم-معاصر-2'), ('الدورة-التعريفية-بالعلوم-الإسلامية', 'الدورة-التعريفية-بالعلوم-الإسلامية'), ('برنامج-برة-الصندوق', 'برنامج-برة-الصندوق'), ('مدخل-إلى-العلوم-الإنسانية', 'مدخل-إلى-العلوم-الإنسانية')], default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='audiocourse',
            name='categroty',
            field=models.CharField(choices=[('عام', 'عام'), ('جذور-قرآنية', 'جذور-قرآنية'), ('ماذا-أتعلم-وكيف-أتعلم', 'ماذا-أتعلم-وكيف-أتعلم'), ('تأسيس-وعي-مسلم-معاصر-2', 'تأسيس-وعي-مسلم-معاصر-2'), ('الدورة-التعريفية-بالعلوم-الإسلامية', 'الدورة-التعريفية-بالعلوم-الإسلامية'), ('برنامج-برة-الصندوق', 'برنامج-برة-الصندوق'), ('مدخل-إلى-العلوم-الإنسانية', 'مدخل-إلى-العلوم-الإنسانية')], default='', max_length=250),
        ),
    ]
