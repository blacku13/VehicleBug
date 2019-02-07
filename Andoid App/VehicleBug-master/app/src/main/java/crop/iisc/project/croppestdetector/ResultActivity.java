package crop.iisc.project.croppestdetector;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import org.json.JSONObject;

public class ResultActivity extends Activity {
    private JSONObject json_object;
    private TextView result;
    private String res;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.result_main);
        try {
            json_object = new JSONObject(getIntent().getStringExtra("information"));
            res = json_object.getString("response");
        }
        catch (Exception e){
            Toast.makeText(this, "something happened bad", Toast.LENGTH_SHORT).show();
            finishActivity(1);
        }
        result = findViewById(R.id.result);
        result.setText(res);



    }

}
