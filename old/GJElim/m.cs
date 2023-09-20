private static void Main(string[] args)
    {
        float[,] matrix = { { 2,1,5},{-3,6,0 } };
        float[] answer = {0,0};
        for(int i=0;i<2;i++)
        {
            if (matrix[i,i] == 0.0)
            {
                Console.WriteLine("Divide by zero detected!");
            }
            for(int j =0;j<2;j++)
            {
                if (i != j)
                {
                    float ratio = matrix[j,i] / matrix[i,i];

                    for (int k = 0; k < 3; k++)
                    {
                        matrix[j, k] = matrix[j, k] - ratio * matrix[i, k];
                    }
                }
                
            }
        }

        for(int i = 0; i < 2; i++)
        {
            answer[i] = matrix[i, 2]/matrix[i,i];
        }
        Console.WriteLine("Required solution is:");
        //for(int i = 0; i < 2; i++)
        //{
        //    Console.Write("X{0} = {1}\t", i, answer[i]);
        //}
        Console.Write("X={0}\t", answer[0]);
        Console.WriteLine("Y={0}\t", answer[1]);
    }