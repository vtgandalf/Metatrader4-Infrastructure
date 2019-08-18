// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: testing_data.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
/// <summary>Holder for reflection information generated from testing_data.proto</summary>
public static partial class TestingDataReflection {

  #region Descriptor
  /// <summary>File descriptor for testing_data.proto</summary>
  public static pbr::FileDescriptor Descriptor {
    get { return descriptor; }
  }
  private static pbr::FileDescriptor descriptor;

  static TestingDataReflection() {
    byte[] descriptorData = global::System.Convert.FromBase64String(
        string.Concat(
          "ChJ0ZXN0aW5nX2RhdGEucHJvdG8aDHN5bWJvbC5wcm90bxoMcGVyaW9kLnBy",
          "b3RvGgxzcHJlYWQucHJvdG8aEXRpbWVfcGVyaW9kLnByb3RvGg9hbGdvcml0",
          "aG0ucHJvdG8imQEKC1Rlc3RpbmdEYXRhEhcKBnN5bWJvbBgBIAEoCzIHLlN5",
          "bWJvbBIXCgZwZXJpb2QYAiABKAsyBy5QZXJpb2QSFwoGc3ByZWFkGAMgASgL",
          "MgcuU3ByZWFkEiAKC3RpbWVfcGVyaW9kGAQgASgLMgsuVGltZVBlcmlvZBId",
          "CglhbGdvcml0aG0YBSABKAsyCi5BbGdvcml0aG1iBnByb3RvMw=="));
    descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
        new pbr::FileDescriptor[] { global::SymbolReflection.Descriptor, global::PeriodReflection.Descriptor, global::SpreadReflection.Descriptor, global::TimePeriodReflection.Descriptor, global::AlgorithmReflection.Descriptor, },
        new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
          new pbr::GeneratedClrTypeInfo(typeof(global::TestingData), global::TestingData.Parser, new[]{ "Symbol", "Period", "Spread", "TimePeriod", "Algorithm" }, null, null, null, null)
        }));
  }
  #endregion

}
#region Messages
public sealed partial class TestingData : pb::IMessage<TestingData> {
  private static readonly pb::MessageParser<TestingData> _parser = new pb::MessageParser<TestingData>(() => new TestingData());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pb::MessageParser<TestingData> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::TestingDataReflection.Descriptor.MessageTypes[0]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public TestingData() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public TestingData(TestingData other) : this() {
    symbol_ = other.symbol_ != null ? other.symbol_.Clone() : null;
    period_ = other.period_ != null ? other.period_.Clone() : null;
    spread_ = other.spread_ != null ? other.spread_.Clone() : null;
    timePeriod_ = other.timePeriod_ != null ? other.timePeriod_.Clone() : null;
    algorithm_ = other.algorithm_ != null ? other.algorithm_.Clone() : null;
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public TestingData Clone() {
    return new TestingData(this);
  }

  /// <summary>Field number for the "symbol" field.</summary>
  public const int SymbolFieldNumber = 1;
  private global::Symbol symbol_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Symbol Symbol {
    get { return symbol_; }
    set {
      symbol_ = value;
    }
  }

  /// <summary>Field number for the "period" field.</summary>
  public const int PeriodFieldNumber = 2;
  private global::Period period_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Period Period {
    get { return period_; }
    set {
      period_ = value;
    }
  }

  /// <summary>Field number for the "spread" field.</summary>
  public const int SpreadFieldNumber = 3;
  private global::Spread spread_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Spread Spread {
    get { return spread_; }
    set {
      spread_ = value;
    }
  }

  /// <summary>Field number for the "time_period" field.</summary>
  public const int TimePeriodFieldNumber = 4;
  private global::TimePeriod timePeriod_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::TimePeriod TimePeriod {
    get { return timePeriod_; }
    set {
      timePeriod_ = value;
    }
  }

  /// <summary>Field number for the "algorithm" field.</summary>
  public const int AlgorithmFieldNumber = 5;
  private global::Algorithm algorithm_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Algorithm Algorithm {
    get { return algorithm_; }
    set {
      algorithm_ = value;
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override bool Equals(object other) {
    return Equals(other as TestingData);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public bool Equals(TestingData other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (!object.Equals(Symbol, other.Symbol)) return false;
    if (!object.Equals(Period, other.Period)) return false;
    if (!object.Equals(Spread, other.Spread)) return false;
    if (!object.Equals(TimePeriod, other.TimePeriod)) return false;
    if (!object.Equals(Algorithm, other.Algorithm)) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override int GetHashCode() {
    int hash = 1;
    if (symbol_ != null) hash ^= Symbol.GetHashCode();
    if (period_ != null) hash ^= Period.GetHashCode();
    if (spread_ != null) hash ^= Spread.GetHashCode();
    if (timePeriod_ != null) hash ^= TimePeriod.GetHashCode();
    if (algorithm_ != null) hash ^= Algorithm.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void WriteTo(pb::CodedOutputStream output) {
    if (symbol_ != null) {
      output.WriteRawTag(10);
      output.WriteMessage(Symbol);
    }
    if (period_ != null) {
      output.WriteRawTag(18);
      output.WriteMessage(Period);
    }
    if (spread_ != null) {
      output.WriteRawTag(26);
      output.WriteMessage(Spread);
    }
    if (timePeriod_ != null) {
      output.WriteRawTag(34);
      output.WriteMessage(TimePeriod);
    }
    if (algorithm_ != null) {
      output.WriteRawTag(42);
      output.WriteMessage(Algorithm);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int CalculateSize() {
    int size = 0;
    if (symbol_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Symbol);
    }
    if (period_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Period);
    }
    if (spread_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Spread);
    }
    if (timePeriod_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(TimePeriod);
    }
    if (algorithm_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Algorithm);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(TestingData other) {
    if (other == null) {
      return;
    }
    if (other.symbol_ != null) {
      if (symbol_ == null) {
        Symbol = new global::Symbol();
      }
      Symbol.MergeFrom(other.Symbol);
    }
    if (other.period_ != null) {
      if (period_ == null) {
        Period = new global::Period();
      }
      Period.MergeFrom(other.Period);
    }
    if (other.spread_ != null) {
      if (spread_ == null) {
        Spread = new global::Spread();
      }
      Spread.MergeFrom(other.Spread);
    }
    if (other.timePeriod_ != null) {
      if (timePeriod_ == null) {
        TimePeriod = new global::TimePeriod();
      }
      TimePeriod.MergeFrom(other.TimePeriod);
    }
    if (other.algorithm_ != null) {
      if (algorithm_ == null) {
        Algorithm = new global::Algorithm();
      }
      Algorithm.MergeFrom(other.Algorithm);
    }
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(pb::CodedInputStream input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 10: {
          if (symbol_ == null) {
            Symbol = new global::Symbol();
          }
          input.ReadMessage(Symbol);
          break;
        }
        case 18: {
          if (period_ == null) {
            Period = new global::Period();
          }
          input.ReadMessage(Period);
          break;
        }
        case 26: {
          if (spread_ == null) {
            Spread = new global::Spread();
          }
          input.ReadMessage(Spread);
          break;
        }
        case 34: {
          if (timePeriod_ == null) {
            TimePeriod = new global::TimePeriod();
          }
          input.ReadMessage(TimePeriod);
          break;
        }
        case 42: {
          if (algorithm_ == null) {
            Algorithm = new global::Algorithm();
          }
          input.ReadMessage(Algorithm);
          break;
        }
      }
    }
  }

}

#endregion


#endregion Designer generated code
