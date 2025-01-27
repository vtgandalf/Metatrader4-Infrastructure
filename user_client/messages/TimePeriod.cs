// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: time_period.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
/// <summary>Holder for reflection information generated from time_period.proto</summary>
public static partial class TimePeriodReflection {

  #region Descriptor
  /// <summary>File descriptor for time_period.proto</summary>
  public static pbr::FileDescriptor Descriptor {
    get { return descriptor; }
  }
  private static pbr::FileDescriptor descriptor;

  static TimePeriodReflection() {
    byte[] descriptorData = global::System.Convert.FromBase64String(
        string.Concat(
          "ChF0aW1lX3BlcmlvZC5wcm90bxoKZGF0ZS5wcm90byJECgpUaW1lUGVyaW9k",
          "EhsKDGluaXRpYWxfZGF0ZRgBIAEoCzIFLkRhdGUSGQoKZmluYWxfZGF0ZRgC",
          "IAEoCzIFLkRhdGViBnByb3RvMw=="));
    descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
        new pbr::FileDescriptor[] { global::DateReflection.Descriptor, },
        new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
          new pbr::GeneratedClrTypeInfo(typeof(global::TimePeriod), global::TimePeriod.Parser, new[]{ "InitialDate", "FinalDate" }, null, null, null, null)
        }));
  }
  #endregion

}
#region Messages
public sealed partial class TimePeriod : pb::IMessage<TimePeriod> {
  private static readonly pb::MessageParser<TimePeriod> _parser = new pb::MessageParser<TimePeriod>(() => new TimePeriod());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pb::MessageParser<TimePeriod> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::TimePeriodReflection.Descriptor.MessageTypes[0]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public TimePeriod() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public TimePeriod(TimePeriod other) : this() {
    initialDate_ = other.initialDate_ != null ? other.initialDate_.Clone() : null;
    finalDate_ = other.finalDate_ != null ? other.finalDate_.Clone() : null;
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public TimePeriod Clone() {
    return new TimePeriod(this);
  }

  /// <summary>Field number for the "initial_date" field.</summary>
  public const int InitialDateFieldNumber = 1;
  private global::Date initialDate_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Date InitialDate {
    get { return initialDate_; }
    set {
      initialDate_ = value;
    }
  }

  /// <summary>Field number for the "final_date" field.</summary>
  public const int FinalDateFieldNumber = 2;
  private global::Date finalDate_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Date FinalDate {
    get { return finalDate_; }
    set {
      finalDate_ = value;
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override bool Equals(object other) {
    return Equals(other as TimePeriod);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public bool Equals(TimePeriod other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (!object.Equals(InitialDate, other.InitialDate)) return false;
    if (!object.Equals(FinalDate, other.FinalDate)) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override int GetHashCode() {
    int hash = 1;
    if (initialDate_ != null) hash ^= InitialDate.GetHashCode();
    if (finalDate_ != null) hash ^= FinalDate.GetHashCode();
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
    if (initialDate_ != null) {
      output.WriteRawTag(10);
      output.WriteMessage(InitialDate);
    }
    if (finalDate_ != null) {
      output.WriteRawTag(18);
      output.WriteMessage(FinalDate);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int CalculateSize() {
    int size = 0;
    if (initialDate_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(InitialDate);
    }
    if (finalDate_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(FinalDate);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(TimePeriod other) {
    if (other == null) {
      return;
    }
    if (other.initialDate_ != null) {
      if (initialDate_ == null) {
        InitialDate = new global::Date();
      }
      InitialDate.MergeFrom(other.InitialDate);
    }
    if (other.finalDate_ != null) {
      if (finalDate_ == null) {
        FinalDate = new global::Date();
      }
      FinalDate.MergeFrom(other.FinalDate);
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
          if (initialDate_ == null) {
            InitialDate = new global::Date();
          }
          input.ReadMessage(InitialDate);
          break;
        }
        case 18: {
          if (finalDate_ == null) {
            FinalDate = new global::Date();
          }
          input.ReadMessage(FinalDate);
          break;
        }
      }
    }
  }

}

#endregion


#endregion Designer generated code
