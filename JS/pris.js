var firebaseConfig = {
    apiKey: "AIzaSyDaU1bXnd_3qvsX0FZz_KAT5QIEsE_KfyA",
    authDomain: "prescription-619d6.firebaseapp.com",
    projectId: "prescription-619d6",
    storageBucket: "prescription-619d6.appspot.com",
    messagingSenderId: "752774153523",
    appId: "1:752774153523:web:7500882042e320566e2a46"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  var Pname, Pid, Pdiag, Pmed1, Pmed2, Pmed3;

  function Ready(){
      Pname = document.getElementById('Nametxt').value;
      Pid = document.getElementById('ID').value;
      Pdiag = document.getElementById('diagnose').value;
      Pmed1 = document.getElementById('med1').value;
      Pmed2 = document.getElementById('med2').value;
      Pmed3 = document.getElementById('med3').value;
  }

  /* Insert Data */
  document.getElementById('insert').onclick = function (){
      Ready();
      firebase.database().ref('Prescriptions/'+Pid).set({
          Nameofpatient:Pname,
          ID: Pid,
          Diagnosis: Pdiag,
          MedA: Pmed1,
          MedB: Pmed2,
          MedC: Pmed3 
      })
  }