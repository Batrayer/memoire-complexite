int nombre_aleatoire(int n)
{
    n = n + 1;
    n++;
    if (n > 1) {
        return rand() % n + 1;    
    }
}