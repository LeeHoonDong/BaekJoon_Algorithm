import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.max;

public class Main {
    static int []dx={-1,1,0,0};
    static int []dy={0,0,-1,1};
    static int answer=0;
    static int R;
    static int C;
    static int [][]arr;
    static int []visited=new int[26];//처음에는 모든 지점을 방문을 하지 않았기 때문에 선언과 동시에 0으로 초기화
    public static void dfs(int i, int j,int cnt){
        //방문했다면
        if(visited[arr[i][j]]==1){
            answer=max(answer,cnt);
            return;
        }
        else{
            visited[arr[i][j]]=1;
            for(int index=0;index<4;index++){
                int ni=i+dx[index];
                int nj=j+dy[index];
                if(0<=ni && ni<R && 0<=nj && nj<C){
                    dfs(ni,nj,cnt+1);
                }
            }
            visited[arr[i][j]]=0;
        }
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R=Integer.parseInt(st.nextToken());
        C=Integer.parseInt(st.nextToken());
        arr=new int[R][C];
        for(int i=0;i<R;i++){
            String str=br.readLine();
            for(int j=0;j<C;j++){
                arr[i][j]=str.charAt(j)-'A';
            }
        }

        dfs(0,0,0);
        System.out.println(answer);
    }
}
