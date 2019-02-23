
int main()
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