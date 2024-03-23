#include<windows.h>
#include<GL/glut.h>
#include<vector>
#include<iostream>

using namespace std;

struct Point
{
    float x, y;
};

vector<Point> p;
vector<Point> inter;

int i=0, j=0;

void init()
{
    glClearColor(1.0, 1.0, 1.0, 0);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0, 0.0, 1.0);
    gluOrtho2D(0.0, 500.0, 0.0, 500.0);
    glFlush();
}

void display()
{

}

void sort1()
{
    int n=inter.size();
    for(int k=0; k<n-1; k++)
    {
        for (int j=k+1; j<n; j++)
        {
            if(inter[k].x>inter[k+1].x)
            {
                Point temp=inter[k];
                inter[k]=inter[k+1];
                inter[k+1]=temp;
            }
        }
    }
}

void add_inter(Point p1, Point p2, float k)
{
    if(k>=min(p1.y, p2.y) && k<=max(p1.y, p2.y))
    {
        float m=(p2.y-p1.y)/(p2.x-p1.x);
        float inter1=p1.x+(1/m)*(k-p1.y);
        Point in;
        in.x=inter1;
        in.y=k;
        inter.push_back(in);
        sort1();
    }

}

void fillPoly()
{
    float xmin=640, xmax=0, ymin=480, ymax=0;
    for(int i=0; i<p.size(); i++)
    {
        if(p[i].x<xmin)
            xmin=p[i].x;
        else if(p[i].x>xmax)
            xmax=p[i].x;
        if(p[i].y<ymin)
            ymin=p[i].y;
        else if(p[i].y>ymax)
            ymax=p[i].y;
    }
    float k=ymin;
    while(k<=ymax)
    {
        //cout<<k;
        for(int i=0; i<p.size(); i++)
        {
            Point p1=p[i];
            Point p2=p[(i+1)%p.size()];
            add_inter(p1, p2, k);
        }
        for(int i=0; i<inter.size(); i+=2)
        {
            Point p1=inter[i];
            Point p2=inter[i+1];
            cout<<p1.x<<" "<<p2.x<<"\n";
            float x=p1.x;
            while(x<p2.x)
            {
                cout<<"in"<<endl;
                glColor3f(1, 0, 0);
                glBegin(GL_POINTS);
                    glVertex2f(x, k);
                glEnd();
                glFlush();
                x+=1;
            }
        }
        k+=1;
        inter.clear();
    }
}

void drawPoly()
{

    glClear(GL_COLOR_BUFFER_BIT);
    //drawBox();
    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_LINE_LOOP);
    for(int k=0; k<p.size(); k++)
    {
        //cout<<pX[k]<<" "<<pY[k]<<endl;
        glVertex2f(p[k].x, p[k].y);
    }
    glEnd();
    glFlush();
}

void mouseFn(int button, int state, int x, int y)
{
    y=500-y;
    if(button==GLUT_LEFT && state==GLUT_DOWN)
    {
            Point p1;
            p1.x=x;
            p1.y=y;
            p.push_back(p1);
            j++;
            if (j>=3)
            {
                //glColor3f(1.0, 0.0, 0.0);
                drawPoly();
            }
    }

    if (button==GLUT_RIGHT_BUTTON && state==GLUT_DOWN)
    {
        fillPoly();
    }
}


int main(int argc,char **argv)
{
    glutInit(&argc,argv);
    glutInitWindowPosition(100,100);
    glutInitWindowSize(500,500);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutCreateWindow("Odd parity");
    init();
    glutDisplayFunc(display);
    glutMouseFunc(mouseFn);
    glutMainLoop();
    return 0;
}
