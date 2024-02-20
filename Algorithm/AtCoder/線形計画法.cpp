/*********************************************
 * 線形計画法（シンプレックス法）            *
 *********************************************/
#include <iostream>  // for cout
#include <stdio.h>   // for printf()

#define N_ROW 4      // 行数
#define N_COL 6      // 列数
#define N_VAR 2      // 変数の数

using namespace std;

/*
 * 計算クラス
 */
class Calc
{
    // 各種変数
    double min, p, d;
    int i, j, k, x, y, flag;

    public:
        void calcLinearProgramming();   // 線形計画法
};

/*
 * 線形計画法
 */
void Calc::calcLinearProgramming()
{
    // 係数行列
    static double a[N_ROW][N_COL] = {
        { 1.0,  2.0,  1.0,  0.0,  0.0, 14.0},
        { 1.0,  1.0,  0.0,  1.0,  0.0,  8.0},
        { 3.0,  1.0,  0.0,  0.0,  1.0, 18.0},
        {-2.0, -3.0,  0.0,  0.0,  0.0,  0.0}
    };

    while (1) {
        // 列選択
        min = 9999;
        for (k = 0; k < N_COL - 1; k++) {
            if (a[N_ROW - 1][k] < min) {
                min = a[N_ROW - 1][k];
                y = k;
            }
        }
        if (min >= 0) break;

        // 行選択
        min = 9999;
        for (k = 0; k < N_ROW - 1; k++) {
            p = a[k][N_COL - 1] / a[k][y];
            if (a[k][y] > 0 && p < min) {
                min = p;
                x = k;
            }
        }

        // ピボット係数
        p = a[x][y];

        // ピボット係数を p で除算
        for (k = 0; k < N_COL; k++)
            a[x][k] = a[x][k] / p;

        // ピボット列の掃き出し
        for (k = 0; k < N_ROW; k++) {
            if (k != x) {
                d = a[k][y];
                for (j = 0; j < N_COL; j++)
                    a[k][j] = a[k][j] - d * a[x][j];
            }
        }
    }

    // 結果出力
    for (k = 0; k < N_VAR; k++) {
        flag = -1;
        for (j = 0; j < N_ROW; j++) {
            // ==== 2016-11-14 UPDATE ===>
            // if (a[j][k] == 1) flag = j;
            if (a[j][k] == 1) {
                flag = j;
            } else if (flag != -1 && a[j][k] != 0) {
                flag = -1;
                break;
            }
            // <=== 2016-11-14 UPDATE ====
        }
        if (flag != -1)
            printf("x%d = %8.4f\n", k, a[flag][N_COL - 1]);
        else
            printf("x%d = %8.4f\n", k, 0.0);
    }
    printf("z  = %8.4f\n", a[N_ROW - 1][N_COL - 1]);
}

/*
 * メイン処理
 */
int main()
{
    try
    {
        // 計算クラスインスタンス化
        Calc objCalc;

        // 線形計画法
        objCalc.calcLinearProgramming();
    }
    catch (...) {
        cout << "例外発生！" << endl;
        return -1;
    }

    // 正常終了
    return 0;
}