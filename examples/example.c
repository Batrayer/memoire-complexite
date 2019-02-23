void tri_a_bulle(int tab[], int taille)
{
    int i,j,tmp;
    for(i=0; i<taille; i++)
    {
        for(j=0; j<taille-1; j++)
        {
            if(tab[j]>tab[j+1])
            {
                tmp=tab[j];
                tab[j]=tab[j+1];
                tab[j+1]=tmp;
            }
        }
    }
}

void tri_a_bulle2(int tab[], int taille)
{
    int i,j,tmp;
    for(i=0; i<taille; i++)
    {
        for(j=0; j<taille-1-i; j++)
        {
            if(tab[j]>tab[j+1])
            {
                tmp=tab[j];
                tab[j]=tab[j+1];
                tab[j+1]=tmp;
            }
        }
    }
}

int puissance(int x,int n)
{
    int i,res=1;
    for(i=1;i<=n;i++)
    {
        res=res*x;
	}
    return res;
}

void concat_deux_vers_un(int tab1[], int taille1, int tab2[], int taille2,int tab3[])
{
    int i;
    for(i=0; i<taille1; i++)
    {
        tab3[i]=tab1[i];
    }
    for(i=0; i<taille2; i++)
    {
        tab3[i+taille1]=tab2[i];
    }
}

int est_narcissique(int n)
{
    int nb_chiffres=1,tmp=n,somme=0,i;
    while(tmp>=10)
    {
        tmp=tmp/10;
        nb_chiffres++;
    }
    tmp=n;
    for(i=0;i<nb_chiffres;i++)
    {
        somme+=puissance(tmp%10,nb_chiffres);
        tmp=tmp/10;
    }
    if(somme==n) return 1;
    return 0;
}

int nombre_aleatoire(int n)
{
    return rand()%n+1;
}