void tri_a_bulle_inverse(int tab[], int taille)
{
    int i, j, tmp;
    for(i=taille-1, i>0; i--)
    {
        for(j=taille-1; j>1; j--)
        {
            if(tab[j]<tab[j-1])
            {
                tmp=tab[j];
                tab[j]=tab[j-1];
                tab[j-1]=tmp;
            }
        }
    }
}