from django.db import models

# Create your models here.

class Pays(models.Model):


    nom = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ('nom',)
        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'
#--------------------------------------------------------  End Pays ------------------------------------------



#--------------------------------------------------------  Organisme ----------------------------------------------

class Organisme(models.Model):
    nom = models.CharField(max_length=100, blank=False)
 
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = 'Organisme'
        verbose_name_plural = 'Organismes'
#--------------------------------------------------------  End Organisme ------------------------------------------

#--------------------------------------------------------  Pays ----------------------------------------------

class Informationvcard(models.Model):


    nom = models.CharField(max_length=100, blank=False,verbose_name = 'Nom')
    prenom = models.CharField(max_length=100, blank=False,verbose_name = 'Prénom')
    nomar = models.CharField(max_length=100, blank=True,null=True,verbose_name = 'Nom en arabe')
    profession = models.CharField(max_length=100, blank=True,null=True,verbose_name = 'Profession')
    prenomar = models.CharField(max_length=100, blank=True,null=True,verbose_name = 'Prénom en arabe')
    telephoneperso1 = models.CharField(max_length=100, blank=True,verbose_name = 'Tél 1')
    telephoneperso2 = models.CharField(max_length=100, blank=True,verbose_name = 'Tél 2')
    telephonepro1 = models.CharField(max_length=100, blank=True,verbose_name = 'Tél 1')
    telephonepro2 = models.CharField(max_length=100, blank=True,verbose_name = 'Tél 2')
    emailperso= models.CharField(max_length=100, blank=True,verbose_name = 'Email')
    emailorganisme1= models.CharField(max_length=100, blank=True,verbose_name = 'Email 1')   
    emailorganisme2= models.CharField(max_length=100, blank=True,verbose_name = 'Email 2')
    Adressepro=models.TextField(blank=True,null=True,verbose_name = 'Adresse')
    fax = models.CharField(max_length=100, blank=True,null=True,verbose_name = 'Fax')
    site_web = models.CharField(max_length=100, blank=True,null=True,verbose_name = 'Site web')
    organisme = models.ForeignKey(Organisme, on_delete=models.CASCADE,verbose_name = 'Organisme')
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE,verbose_name = 'Pays')
    cv_recto=models.FileField(upload_to='files',verbose_name = 'Recto',null=True,blank=True) 
    cv_verso=models.FileField(upload_to='files',verbose_name = 'Verso',null=True,blank=True)
    note=models.TextField(blank=True)
    def __str__(self):
        return self.nom
  
    class Meta:
        ordering = ('nom',)
        verbose_name = 'Carte de visite'
        verbose_name_plural = 'Carte de visite'
#------------------------------------------------------  End Pays ------------------------------------------

